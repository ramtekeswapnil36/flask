import json

from flask import Flask, request
from service import service

app = Flask(__name__)

DEFAULT_STATUS_CODE = "failure"
SUCCESS_STATUS_CODE = "success"

@app.route('/')
def greet():
    return 'Welcome to Python Assignment'

@app.route('/assignment/bookings', methods=['GET'])
def handle_request():
    """
    API endpoint for fetching all bookings
    """
    response = prepare_result_container()
    try:
        response["response"] = service.fetch_all_bookings()
        response["status"] = SUCCESS_STATUS_CODE
    except Exception as error:
        response["error"] = str(error)
        return json.dumps(response)
    else:
        return json.dumps(response)

def prepare_result_container():
    """
    Returns a dict - response
    """
    return {
        "response":{},
        "status":DEFAULT_STATUS_CODE,
        "error": ""
    }

def available_halls():
    data = request.get_json()
    result = {}

    for key, req in data.items():
        halls = get_available_halls(
            req["capacity"],
            req["startTime"],
            req["endTime"]
        )
        result[key] = halls

    return result