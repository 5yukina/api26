#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-4-17 17:10
# Author:ws
# @File:login.py
# @Software:PyCharm
import requests

class xzs_login(object):
    def login(self,username,ps):
        self.url = "http://127.0.0.1:8000/api/user/login"
        self.header = {
            "Content-Type": "application/json"
        }
        self.data={"userName":username,"password":ps,"remember":False}
        r = requests.post(url=self.url,headers=self.header,json=self.data)
        return r.text

if __name__ == '__main__':
    pass