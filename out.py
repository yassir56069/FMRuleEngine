"""Return digest and processing for response from flask service

Usage:
    ./out.py

Author:
    Yassir Hoossan Buksh - last edit 23|08|2023
"""

from flask import Flask
from setup import res

app = Flask(__name__)

if len(res) > 0:
    if len(res) == 1:
        print('There is 1 Notification to send: ')
    else: 
        print(f'There are {len(res)} Notifications to send:')
    
    print(res)
else:
    print('No notifications to send')




@app.route('/')
def test():
    """Test"""
    print('test')
    return 'test. change route with /change'


@app.route('/change/<device>')
def updateDeviceOnOff(device_data:dict):
    print(f'Updating device {device_data["deviceID"]}')
    res = r.onOfflineRule(device_data)
    return jsonify(res)
