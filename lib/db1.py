#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-4-19 16:29
# Author:ws
# @File:db1.py
# @Software:PyCharm
import logging
from config.config import *
import sys
sys.path.append('..')
import pymysql

#创建连接
def conn():
    con = pymysql.connect(
        host=db_host,
        port=db_port,
        db=db,
        user=db_user,
        password=db_ps,
        charset="utf8"
    )
    return con
#封装数据库查询操作
def query_db(sql):
    con = conn()
    cursor = con.cursor()#创建游标
    logging.debug(sql)
    cursor.execute(sql)#利用游标执行sql
    result = cursor.fetchone()#获取执行的结果
    logging.debug(result)
    cursor.close()#关闭游标
    con.close()#关闭连接
    return result#返回执行的结果
#封装更改数据库操作
def change_db(sql):
    con = conn()
    cursor = con.cursor()#创建游标
    try:
        cursor.execute(sql)
        logging.debug(sql)
        con.commit()#如果成功就提交
    except Exception as e:
        logging.error(str(e))
        con.rollback()#如果失败就回滚
    finally:
        cursor.close()#关闭游标
        con.close()#关闭连接
def check_user(name):
    rel = query_db("select * from t_user where user_name='{}'".format(name))
    return True if rel else False#三目运算符
def add_user(name,ps):
    sql = "insert into t_user(user_name,password)values ('{}','{}')".format(name,ps)
    change_db(sql)
def del_user(name):
    sql = "delete from t_user where user_name='{}'".format(name)
    change_db(sql)