from calendar import timegm
from datetime import datetime, timedelta
from flask import Flask, request, jsonify

import sys
import json
import base64
import requests
import _strptime 


app = Flask(__name__)
app.debug = True


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


def get_auth_token():
    '''
        get an auth token
    '''
    URL = 'https://gateway.eu1.mindsphere.io'
    TOKEN_ENDPOINT = '/api/technicaltokenmanager/v3/oauth/token'

    # Payload for getting auth token
    payload = "{\"grant_type\": \"client_credentials\",\"appName\":\"grafana\",\"appVersion\": \"1.0.0\",\"hostTenant\": \"sagtwdev\",\"userTenant\": \"sagtwdev\"}"
    # Encoding of App Credentials in Base64 format
    encoded = base64.b64encode(b'sagtwdev-grafana-1.0.0:TJdNerP2ofc4zb9YTpIbdQvJue5KSMdvXdQQQQQQQQQ (PLEASE REPLACE IT WITH YOUR TOKEN)').decode()
    headers = {
    'X-SPACE-AUTH-KEY': 'Bearer ' + encoded,
    'Content-Type': 'application/json'
    }

    token_res = requests.post(url = URL+TOKEN_ENDPOINT, headers = headers, data = payload)
    data = token_res.json()

    #Token Generated using App Credentials
    token = data['access_token']

    return token


def get_response(_url):
    '''
        send request and get content of respeonse
    '''
    auth_token = get_auth_token()
    response = requests.get(url = _url, auth = BearerAuth(auth_token))

    return response.text


def convert_to_time_ms(timestamp):
    return 1000 * timegm(datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%S.%fZ').timetuple())


@app.route('/')
def health_check():
    return 'This datasource is healthy.'
    
@app.route('/search', methods=['POST'])
def search():
    # Used by the find metric options on the query tab in Grafana panels.
    return jsonify(["Ambient_Temp", "Motor_Temp", "Raw_Vibration_Signal", "aCrest", "vCrest"])

@app.route('/query', methods=['POST'])
def query():
    req = request.get_json()
    _req_attribute = req['targets'][0]['target']

    _asset_id = 'ed68e42a946441bc8b2a2a54ebb174b2'
    _aspect_id = 'aspect_Virtual_Motor_Condition'
    
    _from = req['range']['from']
    _to = req['range']['to']
    _datetime_from = datetime.strptime(req['range']['from'][:19], "%Y-%m-%dT%H:%M:%S")
    _datetime_to = datetime.strptime(req['range']['to'][:19], "%Y-%m-%dT%H:%M:%S")

    # Parse the time range from Grafana panel and then estimate interval value and interval unit
    _interval_point_num = 50
    _interval = int((_datetime_to - _datetime_from).total_seconds()) // _interval_point_num
    _intervalValue = _interval
    if _interval > 86400:
        _intervalUnit = 'day'
        _intervalValue = str(_interval//86400 + 1)
        _datetime_from = _datetime_from.replace(hour=0, minute=0, second=0)
        _datetime_to = _datetime_from + timedelta(days=200*(_interval//86400 + 1))
    elif _interval > 3600:
        _intervalUnit = 'hour'
        _intervalValue = str(_interval//3600 + 1)
        _datetime_from = _datetime_from.replace(minute=0, second=0)
        _datetime_to = _datetime_from + timedelta(hours=200*(_interval//3600 + 1))
    elif _interval > 60:
        _intervalUnit = 'minute'
        _intervalValue = str(_interval//60 + 1)
        _datetime_from = _datetime_from.replace(second=0)
        _datetime_to = _datetime_from + timedelta(minutes=200*(_interval//60 + 1))
    else:
        _intervalUnit = 'second'
        _intervalValue = str(_interval)
        _datetime_to = _datetime_from + timedelta(seconds=200*_interval)

    _from = _datetime_from.strftime("%Y-%m-%dT%H:%M:%SZ")
    _to = _datetime_to.strftime("%Y-%m-%dT%H:%M:%SZ")

    url = "https://gateway.eu1.mindsphere.io/api/iottsaggregates/v3/aggregates/" + _asset_id + "/" + _aspect_id + "?from=" + _from + "&to=" + _to + "&intervalValue=" + _intervalValue + "&intervalUnit=" + _intervalUnit
    response_text = get_response(url)
    jsonObj = json.loads(response_text)

    _datapoints = []
    for item in jsonObj:
        try:
            _datapoints.append([item[_req_attribute]['average'], (convert_to_time_ms(item[_req_attribute]['firsttime']) + convert_to_time_ms(item[_req_attribute]['lasttime']))/2])
        except:
            err = "Can't fetch target attribute!"

    data = [
        {
            "target": req['targets'][0]['target'],
            "datapoints": _datapoints
        }
    ]
    return jsonify(data)

# Used for accepting client post annotations
@app.route('/annotations', methods=['POST'])
def annotations():
    req = request.get_json()
    data = [
        {
            "annotation": 'This is the annotation',
            "time": (convert_to_time_ms(req['range']['from']) +
                     convert_to_time_ms(req['range']['to'])) / 2,
            "title": 'Deployment notes',
            "tags": ['tag1', 'tag2'],
            "text": 'Hm, something went wrong...'
        }
    ]
    return jsonify(data)


# Optional tag
@app.route('/tag-keys', methods=['POST'])
def tag_keys():
    data = [
        # {"type": "string", "text": "City"},
        # {"type": "string", "text": "Country"}
    ]
    return jsonify(data)


# Optional tag
@app.route('/tag-values', methods=['POST'])
def tag_values():
    req = request.get_json()
    if req['key'] == 'City':
        return jsonify([
            # {'text': 'Tokyo'},
            # {'text': 'São Paulo'},
            # {'text': 'Jakarta'}
        ])
    elif req['key'] == 'Country':
        return jsonify([
            # {'text': 'China'},
            # {'text': 'India'},
            # {'text': 'United States'}
        ])

if __name__ == '__main__':
    app.run()