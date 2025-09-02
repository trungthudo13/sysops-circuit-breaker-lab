#!/usr/bin/env bash

docker build -t circuit-breaker:latest . -f ./docker/Dockerfile

docker compose -f ./docker/docker-compose.yaml down

docker compose -f ./docker/docker-compose.yaml up -d