import time, os
import rq
from redis import Redis
from rq import get_current_job
from app import app

#inicia a fila
queue = rq.Queue(app.config["REDIS_QUEUE"], 
        connection=Redis.from_url(app.config["REDIS_URL"]))


avaliable_jobs = ['countdown', 'fibonacci']

def countdown(seconds):
    job = get_current_job()    
    for i in range(seconds):
        job.meta['progress'] = 100.0 * i / seconds
        job.save_meta()        
        time.sleep(1)
    job.meta['progress'] = 100
    job.save_meta()
    return "Ok" # esse valor será colocar no job.result

def enqueue_job(job_name, meta):
    job = queue.enqueue(job_name, meta["seconds"], result_ttl=-1)
    job.meta = meta
    job.save_meta()
    return job

def create_a_job(job_name, meta):
    job_name = 'app.jobs.{}'.format(job_name)
    job = enqueue_job(job_name, meta)
    return job.get_id()

def get_job_status(id):
    job = queue.fetch_job(id)

    job_info = {
        'id': job.get_id(),
        'meta': job.meta,
        'status': job.status,
        'created_at': job.enqueued_at,       
        'started_at': job.started_at,
        'finished_at': job.ended_at,
        'result': job.result
    }

    return job_info