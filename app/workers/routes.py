from app import app, celery

@app.route('/job', methods=['POST'])
def create_job():
    job = celery.bg_job_fibonnacci.delay(5)    
    return jsonify({'job_id' : 'job created !'})

@app.route('/job/<string:job_id>', methods=['POST'])
def get_job():
    return jsonify({'message' : 'job created !'})