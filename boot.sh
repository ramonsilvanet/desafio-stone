#!/bin/sh
# this script is used to boot a Docker container

# inicia o servidor http
exec gunicorn -b :5000 --access-logfile - --error-logfile - application:app