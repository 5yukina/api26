#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-4-15 14:54
# Author:ws
# @File:demo1.py
# @Software:PyCharm
import requests

url = "http://httpbin.org/get"

#
r = requests.get(url)

#
#
print(r.text)
#
print(r.content)
#
print(r.encoding)
#
print(r.headers)
#
print(r.status_code)
#
print(r.cookies)