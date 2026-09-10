# Payment Service Health Dashboard

## Project Overview

This project implements a lightweight Payment Service Health API using Flask.

The application provides basic service information that can be used by engineers and automated monitoring checks.

The project demonstrates an end-to-end Git-to-deployment workflow including:

- Flask API development
- Automated testing using pytest
- Git feature branches and meaningful commits
- Merge conflict creation and resolution
- Docker containerization
- Jenkins CI pipeline
- Simple service health dashboard

## API Endpoints

### 1. Health Endpoint

**Endpoint:**

```text
GET /health
```

Returns the current health status of the payment service.

Example response:

```json
{
  "status": "UP",
  "service": "payment-service"
}
```

### 2. Version Endpoint

**Endpoint:**

```text
GET /version
```

Returns the current application version.

Example response:

```json
{
  "version": "1.1.0"
}
```

### 3. Environment Endpoint

**Endpoint:**

```text
GET /environment
```

Returns the current environment.

The environment value is read from the `ENVIRONMENT` environment variable.

Example response:

```json
{
  "environment": "development"
}
```

## Dashboard

The project includes a simple web-based dashboard that displays:

- Service status
- Application version
- Current environment

Open the dashboard at:

```text
http://localhost:5001/
```

The dashboard retrieves information from the `/health`, `/version`, and `/environment` API endpoints.

## Prerequisites

- Python 3
- Git
- Docker Desktop
- Jenkins

## Local Setup

### 1. Clone the repository

```bash
git clone https://github.com/aashibaksh29/payment-service-health.git
cd payment-service-health
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

The application runs on port `5001`.

## Testing

Run the automated test suite:

```bash
python -m pytest
```

The tests verify the health, version, and environment endpoints.

## Docker

### Build the image

```bash
docker build -t payment-service-health:1.0 .
```

### Run the container

```bash
docker run -d \
  --name payment-service \
  -p 5001:5001 \
  -e ENVIRONMENT=development \
  payment-service-health:1.0
```

### Verify the endpoints

```bash
curl http://localhost:5001/health
curl http://localhost:5001/version
curl http://localhost:5001/environment
```

Open the dashboard at:

```text
http://localhost:5001/
```

### Stop the container

```bash
docker stop payment-service
docker rm payment-service
```

## Jenkins CI Pipeline

The Jenkins pipeline automates the following stages:

1. Checkout
2. Install
3. Test
4. Build
5. Tag
6. Health check

### Pipeline flow

```text
GitHub
   ↓
Checkout
   ↓
Install dependencies
   ↓
Run pytest
   ↓
Build Docker image
   ↓
Tag with Jenkins build number
   ↓
Run container
   ↓
Verify /health
```

The Docker image is tagged using the Jenkins build number.

Example:

```text
payment-service-health:8
```

The health-check stage starts the container and verifies the `/health` endpoint.

## Git Workflow

The project uses the following branch structure:

```text
main
  ↑
develop
  ↑
feature/*
```

Feature branches used:

- `feature/health-endpoint`
- `feature/version-endpoint`
- `feature/docker-container`
- `feature/jenkins-pipeline`
- `feature/dashboard`

Changes were developed on feature branches and merged into `develop`.

The final `develop` branch was merged into `main` through a pull request.

## Merge Conflict Resolution

A controlled merge conflict was intentionally created in `README.md` between `develop` and `feature/version-endpoint`.

The conflicting version information was resolved, the merge was completed successfully, and the automated tests were run again.

## Project Learning

This project demonstrates:

- Git branching and version control
- Feature-based development
- Merge conflict resolution
- Automated testing
- Docker containerization
- Environment-based configuration
- Jenkins CI automation
- Application health verification
