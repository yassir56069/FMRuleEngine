""" Atomic functions containing each rules for processing

Usage:
    python app.py

Author:
    Yassir Hoossan Buksh - last edit 23|08|2023
"""

import time
from durable.lang import *
from durable.engine import *


def device_ruleset(res:list) -> list:
    """Ruleset in place for the device 

    Args:
    res (list): result list to be parsed (for appending information)
    rs (str): the ruleset to be used (default - device)


    Returns:
    list: appends to results list
    """
    with ruleset('device'):
        @when_all(m.online == True)
        def online_status(c):
            res.append('Device {0} is online. time: {1}'.format(c.m.device_id, time.time()))

        @when_all(m.online == False)
        def offline_status(c):
            res.append('Device {0} is offline. time: {1}'.format(c.m.device_id, time.time()))
        
        @when_all(m.status == True)
        def on_status(c):
            res.append('Device {0} is on. time: {1}'.format(c.m.device_id, time.time()))

        @when_all(m.status == False)
        def off_status(c):
            res.append('Device {0} is off. time: {1}'.format(c.m.device_id, time.time()))

    return res