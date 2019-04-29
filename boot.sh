#!/bin/sh
# this script is used to boot a Docker container

# inicia o executor de filas
exec rq worker ${REDIS_QUEUE} -u ${REDIS_URL} &

# inicia o servidor http
exec gunicorn -b :5000 --access-logfile - --error-logfile - application:app
