FROM python:3.6-alpine

RUN adduser -D bgtasks

WORKDIR /home/bg-tasks

COPY requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY app app
COPY application.py config.py boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP=application.py
ENV FLASK_ENV=development
ENV SECURE_KEY=4fa09868ca6e400ce5c9cf7a95872e17

ENV SESSION_TIMEOUT=600

ENV CELERY_BROKER_URL=redis://localhost:6379
ENV CELERY_RESULT_BACKEND=redis://localhost:6379


RUN chown -R bgtasks:bgtasks ./
USER bgtasks

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]