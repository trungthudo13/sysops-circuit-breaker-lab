#!/bin/sh
set -e

echo "[Entrypoint] Running Django setup..."

# Load .env nếu tồn tại (chỉ nhận KEY=VALUE, không có khoảng trắng quanh '=')
if [ -f "/app/.env" ]; then
  echo "[Entrypoint] Loading /app/.env"
  # Xuất tất cả biến khi source, rồi tắt tự động export
  set -a
  # shellcheck disable=SC1091
  . /app/.env
  set +a
fi

# Migrate
echo "[Entrypoint] Applying migrations..."
python manage.py migrate --noinput

# Collect static
echo "[Entrypoint] Collecting static files..."
python manage.py collectstatic --noinput

# Run Daphne
echo "[Entrypoint] Starting Daphne..."
exec daphne -b 0.0.0.0 -p 8000 \
    --proxy-headers \
    --access-log - \
    CircuitBreaker.asgi:application