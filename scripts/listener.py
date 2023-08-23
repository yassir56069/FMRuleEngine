""" Requests class used to digest backend info into durable rules

Usage:
    ./out.py

Author:
    Yassir Hoossan Buksh - last edit 23|08|2023
"""
from durable.lang import *
from durable.engine import *

class Requests:
    def __init__(self, rs:str) -> None:
        self.rs = rs

    def call(self, data:dict):
        try: 
            post(self.rs, data)
        except MessageNotHandledException as error:
            print(f'{error} -- Some rules are not being handled properly')

# try:
#     post('device', {'deviceID': '23r34feijfer0932','onlineStatus' : False, 'status': True})

# except MessageNotHandledException as error:
#     pass

