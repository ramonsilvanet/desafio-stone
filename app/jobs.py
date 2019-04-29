import time, os
import rq
from redis import Redis
from rq import get_current_job
from app import app

#inicia a fila
queue = rq.Queue(app.config["REDIS_QUEUE"], 
        connection=Redis.from_url(app.config["REDIS_URL"]))


def countdown(seconds):
    job = get_current_job()
    for i in range(seconds):
        print("progress", i, "%")
        job.meta['progress'] = 100.0 * i / seconds
        job.save_meta()        
        time.sleep(1)
    print('Job completed')

def enqueue_job(job_name, meta):
    job = queue.enqueue(job_name, meta["seconds"])
    job.meta = meta
    job.save_meta()
    return job

def create_a_job(job_name, meta):
    job_name = 'app.jobs.{}'.format(job_name)
    job = enqueue_job(job_name, meta)
    return job.get_id()

def get_job_status(id):
    job = queue.fetch_job(id)
    return job