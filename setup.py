""" Configuration for rules and listeners. processes flask response

Usage:
    ./out.py

Author:
    Yassir Hoossan Buksh - last edit 23|08|2023
"""

from scripts.listener import Requests

import scripts.rules as r

res = []

# rules --
res = r.onOfflineRule(res)



# listeners for requests --
device_caller = Requests('device')

device_caller.call({'deviceID': '23r34feijfer0932','onlineStatus' : False, 'status': True})
