#!/bin/bash

# enter repository
cd dancing-ducks-lucy

# make sure repository is up to date
git fetch && git reset origin/main --hard

# remove existing docker containers
docker compose -f docker-compose.prod.yml down

# run docker compose to spin up containers with updated files
docker compose -f docker-compose.prod.yml up -d --build
