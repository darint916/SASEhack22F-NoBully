from flask import Blueprint, request
import datetime

from core.api.api_response import APIResponse, AddData, Config

api = Blueprint("api", __name__)

@api.route('/config/get', methods=['GET'])
def get_config():
    return APIResponse.success(Config(200,["google.com", "youtube.com"], ["badword", "badword2"])).make()
    
@api.route('/config/add', methods=['POST'])
def create_config():
    data = request.get_json()
    json_obj = json.dumps(data)

    with open("config.json", "w") as f:
        f.write(json_obj)
    
    return APIResponse.success(AddData(True)).make()

