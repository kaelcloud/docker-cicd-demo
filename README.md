# Docker & CI/CD Pipeline Demo

A hands-on project that containerizes a small Python (Flask) web application with Docker and sets up an automated CI/CD pipeline using GitHub Actions. The pipeline runs tests, builds the Docker image, and smoke-tests the running container on every push.

## What this demonstrates

- Containerizing an application with a **Dockerfile**
- Building and running a **Docker image** locally
- Writing an automated **CI/CD pipeline** with GitHub Actions
- Running automated **tests** and a container **smoke test** on every push
- A **health-check endpoint** suitable for monitoring and Kubernetes liveness probes

## Tech stack

Python, Flask, Docker, GitHub Actions, pytest

## Project structure

```
.
├── app.py                      # Flask web app (home + /health endpoint)
├── requirements.txt            # Python dependencies
├── Dockerfile                  # Container build instructions
├── test_app.py                 # Automated tests
└── .github/workflows/ci-cd.yml # CI/CD pipeline definition
```

## Running locally with Docker

Build the image:

```bash
docker build -t docker-cicd-demo .
```

Run the container:

```bash
docker run -d -p 5000:5000 --name myapp docker-cicd-demo
```

Test it:

```bash
curl http://localhost:5000          # home page
curl http://localhost:5000/health   # {"status": "healthy"}
```

Stop and remove:

```bash
docker stop myapp
docker rm myapp
```

## The CI/CD pipeline

The workflow in `.github/workflows/ci-cd.yml` runs automatically on every push to `main`. It:

1. Checks out the code
2. Sets up Python
3. Installs dependencies
4. Runs automated tests with pytest
5. Builds the Docker image (validating the Dockerfile)
6. Runs the container and smoke-tests the `/health` endpoint

This simulates a lightweight modern release pipeline — every change is automatically tested and validated before it could be deployed.

## How this connects to Kubernetes / AKS

This project produces a container image — the same unit that Kubernetes orchestrates. The `/health` endpoint maps directly to a Kubernetes **liveness/readiness probe**, and the image could be pushed to a registry like **Azure Container Registry (ACR)** and deployed to **AKS**. Containerization is the foundation; Kubernetes is the orchestration layer on top.

---

*Part of my hands-on cloud and DevOps learning portfolio.*
