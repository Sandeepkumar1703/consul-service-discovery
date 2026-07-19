import os
import signal
import atexit
from datetime import datetime
from flask import Flask, jsonify
import consul

SERVICE_NAME = os.getenv("SERVICE_NAME", "service-a")
SERVICE_PORT = int(os.getenv("SERVICE_PORT", "5001"))
CONSUL_HOST = os.getenv("CONSUL_HOST", "consul")
CONSUL_PORT = int(os.getenv("CONSUL_PORT", "8500"))
SERVICE_ID = f"{SERVICE_NAME}-{SERVICE_PORT}"
SERVICE_ADDRESS = os.getenv("SERVICE_ADDRESS", SERVICE_NAME)

app = Flask(__name__)
client = consul.Consul(host=CONSUL_HOST, port=CONSUL_PORT)


def register_service():
    client.agent.service.register(
        name=SERVICE_NAME,
        service_id=SERVICE_ID,
        address=SERVICE_ADDRESS,
        port=SERVICE_PORT,
        check=consul.Check.http(
            f"http://{SERVICE_ADDRESS}:{SERVICE_PORT}/health",
            interval="10s",
            deregister="1m"
        )
    )
    print(f"Registered {SERVICE_NAME} to Consul at {CONSUL_HOST}:{CONSUL_PORT}")


def deregister_service():
    try:
        client.agent.service.deregister(SERVICE_ID)
        print(f"Deregistered {SERVICE_ID} from Consul")
    except Exception as error:
        print(f"Failed to deregister {SERVICE_ID}: {error}")


def handle_shutdown(signum, frame):
    deregister_service()
    raise SystemExit(0)


@app.route("/info")
def info():
    return jsonify(
        service=SERVICE_NAME,
        timestamp=datetime.utcnow().isoformat() + "Z",
    )


@app.route("/health")
def health():
    return jsonify(status="pass")


if __name__ == "__main__":
    signal.signal(signal.SIGTERM, handle_shutdown)
    signal.signal(signal.SIGINT, handle_shutdown)
    atexit.register(deregister_service)

    register_service()
    app.run(host="0.0.0.0", port=SERVICE_PORT)
