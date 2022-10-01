from flask import Blueprint, request

api = Blueprint("api", __name__)

@api.route('/testing', methods=['GET'])
def testing():
    response_body = {
        "message": "Hello World"
    }
    
    return response_body

