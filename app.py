#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_httpauth import HTTPBasicAuth
from itsdangerous import (TimedJSONWebSignatureSerializer
                          as Serializer, BadSignature, SignatureExpired)

app = Flask(__name__)
auth = HTTPBasicAuth()

secure_key =  "4fa09868ca6e400ce5c9cf7a95872e17"
auth_token = None

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
@auth.login_required
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/todo/api/v1.0/tasks/<int:task_id>',  methods=['GET'])
@auth.login_required
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/todo/api/v1.0/tasks', methods=['POST'])
@auth.login_required
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = { 
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }

    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route( '/todo/api/v1.0/tasks/<int:task_id>' , methods=['PUT'])
@auth.login_required
def update_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    if 'title' in request.json and type(request.json['title']) != unicode:
        abort(400)
    if 'description' in request.json and type(request.json['description']) is not unicode:
        abort(400)
    if 'done' in request.json and type(request.json['done']) is not bool:
        abort(400)

    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['description'] = request.json.get('description', task[0]['description'])
    task[0]['done'] = request.json.get('done', task[0]['done'])

    return jsonify({'task': task[0]})


# Authentication and Authorization
@auth.verify_password
def check_credentials_and_give_a_token(username_or_token, password):
    
    valid = verify_token(username_or_token)
    if not valid :
        if not username_or_token == 'stone' or not password == 'pagamentos':
            return False
        else:
            return True
    else:
        return True

@app.route( '/todo/api/v1.0/token', methods=['GET'])
@auth.login_required
def get_key():
    auth_token =  Serializer(secure_key, expires_in = 600)
    return jsonify({ 'token': auth_token.dumps({ 'id': "1" }).decode('ascii') })

def verify_token(token):
    s = Serializer(secure_key)
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None
    except BadSignature:
        return None
    
    if data['id'] == '1':
        return True
    else:
        return None

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

if __name__ == "__main__":
    app.run(debug=True)