#!/bin/sh

docker network create redisnet

docker run --name bgtasks -d -p 8000:5000  --rm bgtasks:latest \
-e REDIS_URL=redis://redis-server:6379/0 \
-e SECRET_KEY= \
--network redisnet

docker run --name redis-server -d -p 6379:6379 redis:3-alpine \
--network redisnet \
--rm redis:latest \
