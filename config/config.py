#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-4-26 15:06
# Author:ws
# @File:config.py
# @Software:PyCharm
import logging
import os

#项目路径
#prj_path是当前文件的绝对路径的上一级，__file__指当前文件
prj_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(prj_path,"data") #数据目录，暂时在项目目录下
test_path = os.path.join(prj_path,"test") #用例目录，暂时在项目目录下
test_case_path = os.path.join(prj_path,'test','case')
log_file = os.path.join(prj_path, 'log',"log.txt")
report_file = os.path.join(prj_path, 'report',"report.html")
data_file = os.path.join(prj_path,"data","test_user_data.xlsx")
test_list_file = os.path.join(prj_path,"test","test_list.txt")
last_fails_file = os.path.join(prj_path,"last_fails.pickle")

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename=log_file,
    #encodings='utf-8',
    filemode='a'
)
#数据库配置
db_host = '127.0.0.1'
db_port = 3306
db_user = 'root'
db_ps = 'root'
db = 'xzs'

#邮件配置
smtp_server = 'smtp.qq.com'
smtp_user = '2312249330@qq.com'
smtp_ps = 'dvscfcjzplcqdhif'
sender = smtp_user
receiver = '2312249330@qq.com'
subject = '接口测试报告'

# 命令行
parser = OptionParser()
parser.add_option("--collect-only",action="store_true",dest="collect_only",help="测试用例名称")
parser.add_option("--makesuite-tag",action="store_true",dest="makesuite-tag",help="测试数据文件")
parser.add_option("--rerun-fails",dest="rerun-fails",dest="store_true",help="测试用例列表文件")

(option,args) = parser.parse_args








if __name__ == '__main__':
    logging.info("接口测试")