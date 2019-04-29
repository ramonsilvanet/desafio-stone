FROM python:3.6-alpine

RUN adduser -D bgtasks

WORKDIR /home/bg-tasks

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
RUN pip install gunicorn

COPY app app
COPY application.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP=application.py
ENV FLASK_ENV=development

ENV SECURE_KEY=4fa09868ca6e400ce5c9cf7a95872e17
ENV SESSION_TIMEOUT=600

ENV REDIS_URL=redis://redis-server:6379/0
ENV QUEUE_NAME =bg-tasks

RUN chown -R bgtasks:bgtasks ./
USER bgtasks

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]