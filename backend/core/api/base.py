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

@api.route('/config/add', methods=['POST'])
def create_config():
    Config.settings = request.get_json()
    return APIResponse.success(AddData(True)).make()

@api.route('/intercept/get', methods=['GET'])
def get_intercept():
    if InterceptedJson.data:
        return APIResponse.success(InterceptedJson).make()
    return APIResponse.error(404, "No data").make()

@api.route('/intercept/report', methods=['POST'])
def report_intercept():
    InterceptedJson.data = request.get_json()
    return APIResponse.success(AddData(True)).make()


