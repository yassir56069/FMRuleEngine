"""Return digest and processing for response from flask service

Usage:
    ./out.py

Author:
    Yassir Hoossan Buksh - last edit 23|08|2023
"""

from flask import Flask, jsonify
from urllib import parse
from setup import res


import scripts.rules as r



if len(res) > 0:
    if len(res) == 1:
        print('There is 1 Notification to send: ')
    else:
        print(f'There are {len(res)} Notifications to send:')

    print(jsonify(res))
else:
    print('No notifications to send')

print(parse.urlencode({'deviceID': '23r34feijfer0932','onlineStatus' : False, 'status': True}))


