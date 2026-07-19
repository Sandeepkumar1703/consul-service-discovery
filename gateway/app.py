import os
from flask import Flask, jsonify, abort
import requests
import consul

CONSUL_HOST = os.getenv("CONSUL_HOST", "consul")
CONSUL_PORT = int(os.getenv("CONSUL_PORT", "8500"))
DISCOVERED_SERVICES = ["service-a", "service-b", "service-c"]

app = Flask(__name__)
client = consul.Consul(host=CONSUL_HOST, port=CONSUL_PORT)


def discover_service(service_name):
    _, nodes = client.catalog.service(service_name)
    if not nodes:
        raise LookupError(f"No healthy instances found for {service_name}")

    node = nodes[0]
    address = node.get("ServiceAddress") or node.get("Address")
    port = node.get("ServicePort")
    return f"http://{address}:{port}"


@app.route("/health")
def health():
    return jsonify(status="pass")


@app.route("/services")
def services():
    return jsonify(services=DISCOVERED_SERVICES)


def forward_request(service_name):
    if service_name not in DISCOVERED_SERVICES:
        abort(404, description=f"Service {service_name} is not configured")

    url = discover_service(service_name)
    response = requests.get(f"{url}/info", timeout=5)
    return jsonify(response.json())


@app.route("/service-a")
def service_a():
    return forward_request("service-a")


@app.route("/service-b")
def service_b():
    return forward_request("service-b")


@app.route("/service-c")
def service_c():
    return forward_request("service-c")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
