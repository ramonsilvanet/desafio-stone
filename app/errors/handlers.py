from app import app
from app.auth import auth, security

from flask import jsonify, make_response


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

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Internal server error'}), 500)