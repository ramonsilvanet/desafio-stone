#!/bin/sh
# this script is used to boot a Docker container

# ativa o virtualenv
source venv/bin/activate
# inicia o servidor http
exec gunicorn -b :5000 --access-logfile - --error-logfile - application:app
