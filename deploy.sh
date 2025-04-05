#!/bin/bash
export PATH="/usr/local/bin:$PATH"

echo "[entrypoint.sh] Starting BookmarkIt app..."

# Go to project root
cd "$(dirname "$0")"

echo "[entrypoint.sh] Pulling latest changes from Git..."
git pull origin main

echo "[entrypoint.sh] Stopping existing containers..."
docker-compose down

echo "[entrypoint.sh] Rebuilding and starting containers..."
docker-compose up -d --build

echo "[entrypoint.sh] Done! App should be live."