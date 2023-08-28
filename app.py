""" Flask application allowing for url routing to parse data into the ruleEngine

Usage:
    python app.py

Author:
    Yassir Hoossan Buksh - last edit 23|08|2023
"""
from urllib import parse
from flask import Flask, jsonify
from scripts.listener import Requests
from setup import res
import requests

RES_LOG_SIZE = 2 # storage of old responses


app = Flask(__name__)

# listeners for requests --
device_caller = Requests('device')



# The API endpoint
URL = "https://iconektback.tech/iconekt/devices-list/7/"

# A GET request to the API
response = requests.get(URL, timeout=5)

# Print the response
res = response.json()


print(parse.urlencode({'deviceID': '23r34feijfer0932','onlineStatus' : False, 'status': True}))


@app.route('/')
def test():
    """Test"""
    print('test')
    return 'test. change route with /update'


@app.route('/update/<device_data>')
def update(device_data:str):
    """update device data"""

    # remove old response
    res.pop()

    device_caller.call(dict(parse.parse_qsl(device_data)))

    return jsonify({'response_query': res})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
