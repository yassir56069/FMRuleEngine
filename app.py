""" Flask application allowing for url routing to parse data into the ruleEngine

Usage:
    python app.py

Author:
    Yassir Hoossan Buksh - last edit 23|08|2023
"""
from urllib import parse
from flask import Flask, jsonify
from scripts.listener import Requests
from setup import out, URL, OUT_LOG_SIZE
import requests



app = Flask(__name__)

# listeners for requests --
device_caller = Requests('device')


# A GET request to the API
response = requests.get(URL, timeout=5)

# Print the response
res = response.json()


print(res)


@app.route('/')
def call_rule():
    """whenever url is accessed rule is processed"""

    if len(out) > OUT_LOG_SIZE:
        out.pop(0)

    device_caller.call(res['tuya_devices'][0])

    return jsonify({'response_query': out})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
