from flask import Blueprint, request
import datetime
import logging
import json

from core.api.api_response import APIResponse, AddData, Config, InterceptedJson

api = Blueprint("api", __name__)

@api.route('/config/get', methods=['GET'])
def get_config():
    if Config.settings:
        return APIResponse.success(Config).make()
    return APIResponse.success(AddData(True)).make()

@api.route('/config/domain/add', methods=['POST'])
def create_domain():
    Config.settings['domain'] = request.get_json()
    return APIResponse.success(AddData(True)).make()

@api.route('/config/block/add', methods=['POST'])
def create_block():
    Config.settings['blockedWords'] = request.get_json()
    return APIResponse.success(AddData(True)).make()

@api.route('/intercept/get', methods=['GET'])
def get_intercept():
    if InterceptedJson.data:
        return APIResponse.success(InterceptedJson).make()
    return APIResponse.error(404, "No data").make()

@api.route('/intercept/report', methods=['POST'])
def report_intercept():
    data = request.get_json()
    fail = True

    if data['Websocket Interceptor']['intercepted']:
        for i in data['Websocket Interceptor']['intercepted']:
            if i['message'] not in InterceptedJson.websocket_messages:
                InterceptedJson.websocket_messages.add(i['message'])
                InterceptedJson.data['Websocket Interceptor']['intercepted'].append(i)

    if data['Http Interceptor']['intercepted']:
        for i in data['Http Interceptor']['intercepted']:
            if i['message'] not in InterceptedJson.http_messages:
                InterceptedJson.http_messages.add(i['message'])
                InterceptedJson.data['Http Interceptor']['intercepted'].append(i)

    return APIResponse.success(AddData(True)).make()
    


