#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-5-9 9:23
# Author:ws
# @File:递归.py
# @Software:PyCharm
def sum(n):
    if n==0:
        return 0
    else:
        return  n+sum(n-1)

print(sum(5))

def factorial(n):
    if n==0:
        return 1
    else:
        return  n*factorial(n-1)

print(factorial(5))