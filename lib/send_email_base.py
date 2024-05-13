#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-4-27 8:45
# Author:ws
# @File:send_email_base.py
# @Software:PyCharm
import smtplib
from email.mime.text import MIMEText
msg = MIMEText('我是测试邮件的正文','plain','utf-8')
msg['From'] = '2312249330@qq.com'
msg['To'] = '2312249330@qq.com'
msg['Subject'] = '接口测试报告主题'
smtp = smtplib.SMTP_SSL('smtp.qq.com')
smtp.login('2312249330@qq.com','dvscfcjzplcqdhif')
smtp.sendmail('2312249330@qq.com',"2312249330@qq.com", msg.as_string())
smtp.quit()