#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-4-27 9:32
# Author:ws
# @File:send_email_att.py
# @Software:PyCharm
import smtplib
from email.mime.text import MIMEText
#支持附件
from email.mime.multipart import MIMEMultipart
#用于使用中文邮件主题
from email.header import Header

#读取report的内容  放到变量  email_body中
with open("../report/report.html", encoding='utf-8')as f:
    email_body = f.read()

#plain指普通文本格式邮件内容
#msg = MIMEText('我是测试邮件的正文','plain','utf-8')
msg = MIMEMultipart()
msg.attach(MIMEText(email_body,'html','utf-8'))
#发件人
msg['From'] = '2312249330@qq.com'
#收件人
msg['To'] = '2312249330@qq.com'
#邮件的标题
msg['Subject'] = Header('接口测试报告','utf-8)')

#上传附件
#构建附件1，传送当前目录下的report.html  文件
att1 = MIMEText(open('../report/report.html', 'rb').read(), 'base64', 'utf-8')#二进制格式打开
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="report.html"'#filename附件显示的名字
msg.attach(att1)

#建立连接
smtp = smtplib.SMTP_SSL('smtp.qq.com')

#登录邮箱
smtp.login('2312249330@qq.com','dvscfcjzplcqdhif')

#发送邮件
smtp.sendmail('2312249330@qq.com',"2312249330@qq.com", msg.as_string())
smtp.quit()