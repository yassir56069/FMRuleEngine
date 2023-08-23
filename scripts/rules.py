""" Atomic functions containing each rules for processing

Usage:
    python app.py

Author:
    Yassir Hoossan Buksh - last edit 23|08|2023
"""

from durable.lang import *
from durable.engine import *
import time

def onOfflineRule(res:list, rs:str = 'device') -> list:
    """Rule determining if device is online or offline.

    Args:
    res (list): result list to be parsed (for appending information)
    rs (str): the ruleset to be used (default - device)


    Returns:
    list: appends to results list
    """
    with ruleset(rs):
        @when_all(m.onlineStatus == 'True')
        def online_status(c):
            res.append('Device {0} is online. time: {1}'.format(c.m.deviceID, time.time()))

        @when_all(m.onlineStatus == 'False')
        def offline_status(c):
            res.append('Device {0} is offline. time: {1}'.format(c.m.deviceID, time.time()))

    return res

# def statusRule(res:list, rs:str = 'device') -> list:
#     """Rule determining if device is on or off.

#     Args:
#         res (list): result list to be parsed (for appending information)
#         rs (str): the ruleset to be used (default - device)


#     Returns:
#         list: appends to results list
#     """
#     with ruleset(rs):
#         @when_all(m.status == 'True')
#         def on_status(c):
#             res.append({'Device {0} is on'.format(c.m.deviceID)})

#         @when_all(m.status == 'False')
#         def off_status(c):
#             res.append({'Device {0} is off'.format(c.m.deviceID)})

#     return res



# from durable.lang import *
# from durable.engine import Ruleset

# class deviceRules(ruleset):
#     """Handles and keeps track of all rule denotions made for devices. Seperate device rule types are stored accordingly, each rule is 

#     Args:
#         ruleset (_type_): _description_
#     """

#     def __init__(self, name):

#        super().__init__(name)

#     def check_status(self, ruleName):
#        with self(ruleName):
#             @when_all(m.subject == 'world')
#             def say_hello(c):
#                print('hello {0}'.format(c.m.subject))
          

# # Tests derived from examples on Durable website.
# printed_value = '?'
# def mock_print(s):
#   global printed_value
#   printed_value = s
#   return s

# def test_hello(builder):
#   device_rules = ruleset
#   with device_rules('test_hello'):
#     @when_all(m.subject == 'World')
#     def say_hello(c):
#       print('Hello {0}'.format(c.m.subject))

#   post('test_hello', { 'subject': 'World' })
  
# test_hello('y')