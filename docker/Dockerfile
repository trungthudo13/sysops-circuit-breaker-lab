# ================================
# Stage 1: Base
# ================================
FROM python:3.13.7-slim AS base

# Environments
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/usr/local/bin:$PATH"

# Update packages & install deps (build-essential cho pip compile, psycopg2…)
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       build-essential \
       curl \
       netcat-traditional \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# ================================
# Stage 2: Install dependencies
# ================================
FROM base AS builder

COPY ./src/requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# ================================
# Stage 3: Runtime
# ================================
FROM base AS runtime

WORKDIR /app

# Copy Python packages từ builder
COPY --from=builder /usr/local/lib/python3.13 /usr/local/lib/python3.13
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy source Django
COPY ./src /app
COPY ./docker/.env /app/.env
COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Healthcheck
# HEALTHCHECK --interval=30s --timeout=5s --start-period=20s --retries=3 \
#   CMD curl -fsS http://127.0.0.1:${PORT}/healthz || exit 1
  
ENTRYPOINT ["/entrypoint.sh"]