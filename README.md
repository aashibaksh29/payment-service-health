# Payment Service Health Dashboard

## Project Overview

This project implements a lightweight Payment Service Health API using Flask.

The application provides basic service information that can be used by
engineers and automated monitoring checks.

The project demonstrates an end-to-end Git-to-deployment workflow including:

- Flask API development
- Automated testing using pytest
- Git feature branches and meaningful commits
- Merge conflict creation and resolution
- Docker containerization
- Jenkins CI pipeline

## API Endpoints

### 1. Health Endpoint

**Endpoint:**

```text
GET /health



## Dashboard

The project includes a simple web-based dashboard that displays:

- Service status
- Application version
- Current environment

Open the dashboard at:

http://localhost:5001/

The dashboard retrieves information from the `/health`, `/version`,
and `/environment` API endpoints.