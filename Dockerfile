FROM python:3.6-alpine

RUN adduser -D bgtasks

WORKDIR /home/bg-tasks

RUN apk add --update gcc libc-dev fortify-headers linux-headers && rm -rf /var/cache/apk/*

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY application.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP=application.py
ENV FLASK_ENV=production

ENV SECURE_KEY=4fa09868ca6e400ce5c9cf7a95872e17
ENV SESSION_TIMEOUT=600

ENV REDIS_SERVER=redis-server
ENV REDIS_PORT=6379/0
ENV REDIS_URL=redis://${REDIS_SERVER}:${REDIS_PORT}}
ENV REDIS_QUEUE=bg-tasks
ENV TESTING=False

RUN chown -R bgtasks:bgtasks ./
USER bgtasks

ENTRYPOINT ["./boot.sh"]