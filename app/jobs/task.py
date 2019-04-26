import time
from app.celery import celery
from app.jobs import bp
from flask import jsonify

@celery.task(bind=True)
def long_job(seconds=100):
    print("Starting task")
    for i in range(seconds):
        print(i)
        time.sleep(1)
    print("Task completed")


@bp.route("/job", methods=['POST'])
def create_job():
    job = long_job.apply_async()
    return jsonify({'job_id': job.id}), 201

@bp.route("/job/<job_id>", methods=['GET'])
def job_status(job_id):
    job = long_job.AsyncResult(job_id)

    if job.state == 'PENDING':
        response = {
            'job_id': job.id,
            'state': job.state,
            'current': 0,
            'total': 1,
            'status': 'Pending...'
        }
    elif job.state != 'FAILURE':
        response = {
            'job_id': job.id,
            'state' : job.state,
            'current' : job.info.get('current', 0),
            'total': job.info.get('total', 1),
            'status': job.info.get('status', '')
        }
        if 'result' in task.info:
            response['result'] = job.info['result']
    else:
        response = {
            'job_id': job.id,
            'state': job.state,
            'current': 1,
            'total': 1,
            'status': str(job.info)
        }
    return jsonify(response)