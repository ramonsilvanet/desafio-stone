import os, time
from celery import Celery
from app import app

app.config.update(
    CELERY_BROKER_URL=os.environ['CELERY_BROKER_URL'],
    CELERY_RESULT_BACKEND=os.environ['CELERY_RESULT_BACKEND']
)

def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL']
    )
    celery.conf.update(app.config)

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    return celery

celery = make_celery(app)


@celery.task
def bg_job_fibonnacci(n):    
    return fibonnacci(n)

def fibonnacci(n):
    # para simular um job realmente lento
    time.sleep(1)
    
    if n < 2:
        return n        
    return fibonnacci(n-1) + fibonnacci(n-2)