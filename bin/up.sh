#!/usr/bin/bash
COMMIT=$(git rev-parse --short HEAD)
DOCKER_TAG="$COMMIT" docker compose up --build $@