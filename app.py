
from urllib import parse

from flask import Flask, jsonify
from scripts.listener import Requests
from setup import res

app = Flask(__name__)

# listeners for requests --
device_caller = Requests('device')

@app.route('/')
def test():
    """Test"""
    print('test')
    return 'test. change route with /update'


@app.route('/update/<device_data>')
def update(device_data:str):
    """update device data"""
    device_caller.call(dict(parse.parse_qsl(device_data)))

    return jsonify({'response_query': res})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
