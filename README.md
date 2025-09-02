# Circuit Breaker Lab (Django + DRF + Daphne)

This demo environment showcases Circuit Breaker behavior implemented with Django and Django REST framework (DRF), running under the Daphne ASGI webserver. The system includes three services (frontier, midline, backline) that call one another to simulate successful and timeout scenarios and observe application‑level Circuit Breaker reactions.

## Tech Stack
- Django + DRF: Build APIs via `rest_framework.views.APIView`.
- Daphne: ASGI webserver, entrypoint `CircuitBreaker.asgi:application`.
- Nginx: Reverse proxy to the `frontier` service (host port 8001).
- Docker/Compose: Packaging and running multiple services.

## Build and Run
- Build/run script: `./dockerc.sh`
  - Builds the image `circuit-breaker:latest` from `docker/Dockerfile`.
  - Starts services via `docker/docker-compose.yaml` (frontier, midline, backline, nginx).

Execute:
```
./dockerc.sh
```

Once running, access via Nginx at: `http://localhost:8001/`

## Key APIs
Routes are mounted per app. Quick reference:
- Frontier (public via Nginx, port 8001):
  - `GET /api/success-request`
  - `GET /api/timeout-request`
- Midline and Backline (internal in the compose network) expose the same routes to form a call chain.

Disable Circuit Breaker per request via query param:
- `?non_circuit_breaker=1`

Examples:
```
curl "http://localhost:8001/api/success-request"
curl "http://localhost:8001/api/timeout-request"
curl "http://localhost:8001/api/timeout-request?non_circuit_breaker=1"
```

## API Docs (OpenAPI/Swagger)
- OpenAPI schema: `GET /api/schema/`
- Swagger UI: `GET /api/schema/swagger-ui/`

Via Nginx (host):
- `http://localhost:8001/api/schema/`
- `http://localhost:8001/api/schema/swagger-ui/`

## Relevant Configuration
- ASGI: `src/CircuitBreaker/asgi.py` and Daphne entrypoint in `docker/entrypoint.sh`.
- Base DRF view: `src/apps/sharedapp/apis/proxyrequest.py` (handles `non_circuit_breaker`, returns 503 when circuit is open, 502 for transient errors).
- Compose: `docker/docker-compose.yaml` (defines the 3 services and Nginx proxy on port 8001).
- Nginx config: `configs/nginx.conf` (upstream to `frontier:8000`).

## Ops Notes
- On first start, the container runs `migrate` and `collectstatic` automatically (see `docker/entrypoint.sh`).
- Environment variables that link service calls are set in compose (e.g., `FRONTIER_DOMAIN`, `MIDLINE_DOMAIN`, `BACKLINE_DOMAIN`).

## Local Development (optional)
- Requires Python 3.13 if running outside Docker.
- Install dependencies from `src/requirements.txt` and run `python src/manage.py runserver`, or start Daphne manually.

---
Contact: If you want to extend the test scenarios (add routes, error/timeout ratios) or integrate metrics/exporters, I can add detailed guidance.
