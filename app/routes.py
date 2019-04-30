from flask import jsonify, request
from app import app, jobs
from app.authentication import auth
from app.errors import bad_request, error_response


@app.route("/job", methods=['POST'])
@auth.login_required
def create_job():
    data = request.get_json() or {}

    if 'job_name' not in data:
        return bad_request("you must specify a job !!!")    
    else:
        job_id = jobs.create_a_job(data['job_name'], data['meta'])

        response = jsonify({"id": job_id, "message": "Job created !!!"})
        response.status_code = 201 # created
        return response     

@app.route("/job/<id>", methods=['GET'])
@auth.login_required
def get_job(id):
    job_info = jobs.get_job_status(id)
    
    if not job_info is None:    
        return jsonify(job_info)
    else:
        return error_response(404, "job not found")