# Monolith_vs_MicroService

This repository provides a simple example of transforming a monolithic application into a microservices architecture.

## Overview

The repository contains:

- A **monolithic application** (`monolith_app.py`) that handles both user and product management.
- Two independent **microservices**:
  - **User Service** (`user_service/user_service.py`) for handling user data.
  - **Product Service** (`product_service/product_service.py`) for handling product data.
- A **Docker Compose** configuration (`docker-compose.yml`) to deploy the microservices together.

## How to Run

### Monolithic Mode

```bash
python monolith_app.py
```
Endpoints:
- Users: [http://localhost:5000/users](http://localhost:5000/users)
- Products: [http://localhost:5000/products](http://localhost:5000/products)

### Microservices Mode

#### Individual Deployment

- **User Service**:
  ```bash
  python user_service/user_service.py
  ```
  [http://localhost:5001/users](http://localhost:5001/users)

- **Product Service**:
  ```bash
  python product_service/product_service.py
  ```
  [http://localhost:5002/products](http://localhost:5002/products)

#### Full Deployment with Docker Compose

```bash
docker-compose up --build
```
This will start both microservices.
