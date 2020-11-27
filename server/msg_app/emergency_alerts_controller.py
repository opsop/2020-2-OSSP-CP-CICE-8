from flask import Flask, request
from flask_restplus import Api, Resource, fields, Namespace
import json
from msg_app import emergency_alerts_service


class EmergencyAlertsDto:
    api = Namespace('emergency_alerts', description='emergency alerts operations')
    city = api.model('city', {
        'city': fields.String(required=False, description='city information')
    })


api = EmergencyAlertsDto.api
_city = EmergencyAlertsDto.city


@api.route('/city_info')
class CityInfo(Resource):
    def get(self):
        return "DONE"

    @api.response(200, 'OK')
    @api.response(400, 'Bad Request')
    @api.response(500, 'Internal Server Error')
    @api.doc('get emergency alerts of a city')
    @api.expect(_city, validate=True)
    def post(self):
        body = json.loads(request.data)
        # req = request.get_json()
        params = body["action"]["params"]
        return emergency_alerts_service.emergency_alerts(params)