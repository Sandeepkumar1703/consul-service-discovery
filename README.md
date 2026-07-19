# Consul Service Discovery Demo

A DevOps portfolio project demonstrating **Service Discovery using HashiCorp Consul**, **Docker Compose**, **Python Flask Microservices**, and an **API Gateway**.

## Project Page

This project was built as part of the roadmap.sh DevOps Projects:

https://roadmap.sh/projects/service-discovery

## GitHub Repository

https://github.com/Sandeepkumar1703/consul-service-discovery

---

# Overview

This project demonstrates how service discovery works in a microservices architecture.

Three independent Flask microservices register themselves with **HashiCorp Consul** when they start. An API Gateway dynamically discovers healthy service instances from Consul and forwards client requests without using hardcoded IP addresses.

---

# Architecture

```
                         Client
                            |
                            |
                            v
                     API Gateway
                       Port:5000
                            |
                            |
                            v
                  Consul Service Registry
                       Port:8500
                            |
      ------------------------------------------------
      |                     |                        |
      |                     |                        |
      v                     v                        v

 Service A             Service B               Service C
 Port:5001             Port:5002               Port:5003
```

Workflow:

1. Services start.
2. Each service registers itself with Consul.
3. Consul performs periodic health checks.
4. API Gateway queries Consul for healthy instances.
5. Gateway forwards requests to the appropriate service.

---

# Features

- Service Discovery using HashiCorp Consul
- Automatic service registration
- Health checks for every service
- Dynamic service lookup
- API Gateway pattern
- Docker Compose orchestration
- Python Flask microservices
- Container networking

---

# Tech Stack

- Python 3.12
- Flask
- HashiCorp Consul
- Docker
- Docker Compose
- REST API
- python-consul

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

Install the following before running the project.

- Docker Desktop
- Docker Compose
- Git

Verify installation:

```bash
docker --version
docker compose version
git --version
```

---

# Clone the Repository

```bash
git clone https://github.com/Sandeepkumar1703/consul-service-discovery.git

cd consul-service-discovery
```

---

# Run the Project

Build and start all services:

```bash
docker compose up --build
```

The following containers will start:

| Component | Port |
|-----------|------|
| Consul | 8500 |
| API Gateway | 5000 |
| Service A | 5001 |
| Service B | 5002 |
| Service C | 5003 |

---

# Consul Dashboard

Open:

```
http://localhost:8500
```

You should see:

- service-a
- service-b
- service-c

All services should appear healthy.

---

# API Endpoints

## Gateway Health

```
GET http://localhost:5000/health
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

## List Registered Services

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

Each Flask microservice automatically registers itself with Consul when it starts.

The registration includes:

- Service name
- Service address
- Port
- Health check endpoint

Registration Flow

```
Service Startup
      |
      |
      v
Register with Consul
      |
      |
      v
Consul Registry
      |
      |
Health Monitoring
```

---

# How the API Gateway Works

The API Gateway never stores service IP addresses.

Instead, it queries Consul to discover healthy service instances.

Request Flow

```
Client
   |
   |
   v
API Gateway
   |
   | Query Consul
   |
   v
Consul
   |
   | Return healthy instance
   |
   v
Requested Service
   |
   |
   v
Response
```

This enables services to move, restart, or scale without changing the gateway configuration.

---

# Health Checks

Each service exposes:

```
GET /health
```

Consul periodically checks this endpoint.

If a service becomes unhealthy, Consul automatically removes it from the list of healthy instances used by the gateway.

---

# Testing Using cURL

Gateway Health

```bash
curl http://localhost:5000/health
```

Service A

```bash
curl http://localhost:5000/service-a
```

Service B

```bash
curl http://localhost:5000/service-b
```

Service C

```bash
curl http://localhost:5000/service-c
```

Registered Services

```bash
curl http://localhost:5000/services
```

---

# Docker Commands

Start containers

```bash
docker compose up --build
```

View running containers

```bash
docker ps
```

View logs

```bash
docker compose logs
```

Stop containers

```bash
docker compose down
```

Rebuild

```bash
docker compose up --build
```

---

# Key Concepts Demonstrated

- Microservices Architecture
- Service Discovery
- Service Registration
- HashiCorp Consul
- Health Checks
- API Gateway Pattern
- Docker Networking
- Container Orchestration
- REST APIs

---

# Future Improvements

- Load balancing across multiple instances
- JWT authentication
- Kubernetes deployment
- Kubernetes service discovery
- GitHub Actions CI/CD
- Prometheus monitoring
- Grafana dashboards

---

# Author

**Sandeep Kumar Prasad**

GitHub: https://github.com/Sandeepkumar1703