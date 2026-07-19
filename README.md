# Consul Service Discovery Demo

GitHub Repository:
https://github.com/Sandeepkumar1703/consul-service-discovery

A DevOps portfolio project demonstrating **service discovery using HashiCorp Consul**, **Docker Compose orchestration**, and a **Python Flask API Gateway**.

The goal of this project is to understand how microservices register themselves with Consul, how services are discovered dynamically, and how an API Gateway routes requests to healthy service instances.

---

# Architecture

```
                         Client
                           |
                           |
                           v
                    API Gateway
                    Port: 5000
                           |
                           |
                           v
                 Consul Service Discovery
                    Port: 8500
                           |
        -------------------------------------
        |                 |                 |
        v                 v                 v

   Service A          Service B          Service C
   Port: 5001         Port: 5002         Port: 5003
```

Each microservice registers itself with Consul during startup.

The API Gateway queries Consul to discover available services and forwards incoming requests to healthy service instances.

---

# Tech Stack

- Python 3.12
- Flask REST API
- HashiCorp Consul
- Docker
- Docker Compose
- REST APIs
- Service Discovery Pattern
- API Gateway Pattern
- Container Networking

---

# Project Structure

```
consul-service-discovery/
│
├── docker-compose.yml
├── README.md
│
├── consul/
│   └── config/
│
├── gateway/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── service-a/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── service-b/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
└── service-c/
    ├── app.py
    ├── Dockerfile
    └── requirements.txt
```

---

# Prerequisites

Before running the project, install:

- Docker
- Docker Compose
- Git

Verify installation:

```bash
docker --version

docker compose version
```

---

# Running the Project

## Clone Repository

```bash
git clone https://github.com/Sandeepkumar1703/consul-service-discovery.git
```

Navigate to project directory:

```bash
cd consul-service-discovery
```

---

## Start Application

Build and start all containers:

```bash
docker compose up --build
```

This will start:

| Component | Port |
|---|---|
| Consul | 8500 |
| API Gateway | 5000 |
| Service A | 5001 |
| Service B | 5002 |
| Service C | 5003 |

---

# Consul Dashboard

Open the Consul UI:

```
http://localhost:8500
```

You should see registered services:

```
service-a
service-b
service-c
```

Consul continuously monitors the health of these services.

---

# API Endpoints

## Gateway Health Check

```
GET http://localhost:5000/health
```

Example:

```json
{
  "status": "healthy"
}
```

---

## Service A

```
GET http://localhost:5000/service-a
```

---

## Service B

```
GET http://localhost:5000/service-b
```

---

## Service C

```
GET http://localhost:5000/service-c
```

---

## List Available Services

```
GET http://localhost:5000/services
```

---

# Example Response

```json
{
  "service": "service-a",
  "timestamp": "2026-07-19T14:22:12.345678Z"
}
```

---

# How Service Registration Works

When a microservice starts:

1. The service connects to Consul.
2. The service registers its name and port.
3. A health check endpoint is registered.
4. Consul stores the service information.
5. Consul continuously checks service availability.

Example flow:

```
Service A
    |
    |
    | Register Service
    |
    v
Consul Service Registry
```

After registration, Consul maintains information like:

```
Service Name     Port

service-a        5001
service-b        5002
service-c        5003
```

---

# How API Gateway Uses Service Discovery

The API Gateway does not store fixed IP addresses.

Instead, it discovers services dynamically through Consul.

Request flow:

```
Client
  |
  |
  v
API Gateway
  |
  |
  | Ask Consul:
  | "Where is service-a?"
  |
  v
Consul
  |
  |
  | Returns healthy instance
  |
  v
Service A
  |
  |
Response
```

This allows services to scale or move without changing gateway configuration.

---

# Health Checks

Each service exposes:

```
GET /health
```

Example:

```
Consul
   |
   |---- Check Service A
   |
   |---- Check Service B
   |
   |---- Check Service C
```

If a service becomes unavailable, Consul marks it unhealthy and prevents routing traffic to it.

---

# Testing With Curl

Gateway health:

```bash
curl http://localhost:5000/health
```

Service A:

```bash
curl http://localhost:5000/service-a
```

Service B:

```bash
curl http://localhost:5000/service-b
```

Service C:

```bash
curl http://localhost:5000/service-c
```

---

# Docker Commands

## View Running Containers

```bash
docker ps
```

## View Logs

```bash
docker compose logs
```

## Stop Application

```bash
docker compose down
```

## Rebuild Application

```bash
docker compose up --build
```

---

# Key Concepts Demonstrated

This project demonstrates:

- Microservices architecture
- Service registration
- Service discovery
- Consul service registry
- Health monitoring
- API Gateway pattern
- Docker containerization
- Docker Compose orchestration
- Container networking
- Dynamic service communication

---

# Future Improvements

Possible enhancements:

- Add authentication using JWT
- Add load balancing between multiple service instances
- Deploy using Kubernetes
- Use Kubernetes Service Discovery
- Add CI/CD pipeline with GitHub Actions
- Add monitoring using Prometheus and Grafana

---

# Author

**Sandeep Kumar Prasad**

GitHub:
https://github.com/Sandeepkumar1703