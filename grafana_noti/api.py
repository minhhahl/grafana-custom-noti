import os
import requests
import logging

from flask import Flask, request
from flask_restful import Resource, Api
from grafana_noti.authentication import auth

SMS_ENDPOINT = os.getenv('SMS_ENDPOINT', 'http://127.0.0.1:8009/sendsms')
SMS_BRANDNAME = os.getenv('SMS_BRANDNAME', 'ELK')
SMS_RECIEVERS = os.getenv('SMS_RECIEVERS', '098123;098456').split(";")
SMS_REQUEST_TIMEOUT = int(os.getenv('SMS_REQUEST_TIMEOUT', 5))


class Ping(Resource):
    def get(self):
        return {'data': 'pong'}


class GrafanaWebHook(Resource):
    def make_request(self, request_url, params):
        logging.info(" ** Send request to", request_url, params)

        req = requests.get(
            request_url,
            verify=False,
            params=params,
            timeout=SMS_REQUEST_TIMEOUT
        )
        return req.status_code == 200

    def send_sms(self, text):
        logging.info(" ** Send alert content to SMS", text)

        for number in SMS_RECIEVERS:
            params = {
                'from': SMS_BRANDNAME,
                'to': number,
                'text': text
            }
            try:
                self.make_request(SMS_ENDPOINT, params)
            except Exception:
                logging.exception("Failed to send sms")

    @auth.login_required
    def post(self):
        payload = request.json

        alert = "{} | {}".format(payload['title'], payload['message'])

        self.send_sms(alert)

        return {'data': 'ok'}


app = Flask(__name__)
api = Api(app)
api.add_resource(Ping, '/ping')
api.add_resource(GrafanaWebHook, '/grafana')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
