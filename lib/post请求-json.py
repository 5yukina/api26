#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-4-15 16:00
# Author:ws
# @File:post请求-json.py
# @Software:PyCharm
import requests

url = "http://httpbin.org/post"
data = '''{
    "name":"zhangsan",
    :age":18
}'''#data =
'{"name":"zhangsan","age":18}'

r = requests.post(url=url,data=data)
print(r.text)