""" Configuration for rules and listeners. processes flask response

Usage:
    python app.py

Author:
    Yassir Hoossan Buksh - last edit 23|08|2023
"""
import scripts.rules.Device_ruleset as dr


OUT_LOG_SIZE = 10 # storage of old responses

out = []


# API endpoint
URL = "https://iconektback.tech/iconekt/devices-list/7/"


# rules --
out = dr.device_ruleset(out)
# res = r.statusRule(res)


# # listeners for requests --
# device_caller = Requests('device')

# device_caller.call({'deviceID': '23r34feijfer0932','onlineStatus' : False, 'status': True})
