from flask import Flask, request
# from flask_restplus import Api, Resource, fields, Namespace

import json
import emergency_alerts_service

app = Flask(__name__)


@app.route('/city_info', methods=['POST'])
def post():
    body = json.loads(request.data)
    # req = request.get_json()
    params = body["action"]["params"]
    return emergency_alerts_service.emergency_alerts(params)


app.run(host='0.0.0.0')