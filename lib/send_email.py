#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time:2024-4-28 14:35
# Author:ws
# @File:send_email.py
# @Software:PyCharm
import smtplib
from email.mime.text import MIMEText
#支持附件
from email.mime.multipart import MIMEMultipart
#用于使用中文邮件主题
from email.header import Header
from config.config import *

def send_email(report_file):
    #读取report的内容  放到变量  email_body中
    with open(report_file,encoding='utf-8')as f:
        email_body = f.read()

    #plain指普通文本格式邮件内容
    #msg = MIMEText('我是测试邮件的正文','plain','utf-8')
    msg = MIMEMultipart()
    msg.attach(MIMEText(email_body,'html','utf-8'))
    #发件人
    msg['From'] = sender
    #收件人
    msg['To'] = receiver
    #邮件的标题
    msg['Subject'] = Header(subject,'utf-8)')

    #上传附件
    #构建附件1，传送当前目录下的report.html  文件
    att1 = MIMEText(open(report_file,'rb').read(),'base64','utf-8')#二进制格式打开
    att1["Content-Type"] = 'application/octet-stream'
    att1["Content-Disposition"] = 'attachment; filename="report.html"'#filename附件显示的名字
    msg.attach(att1)
    try:
        #建立连接
        smtp = smtplib.SMTP_SSL(smtp_server)
        #登录邮箱
        smtp.login(smtp_user,smtp_ps)
        #发送邮件
        smtp.sendmail(sender,receiver,msg.as_string())
        logging.info("====================发送邮件成功====================")
    except Exception as e:
        logging.error(str(e))
    finally:
        smtp.quit()

if __name__ == '__main__':
    send_email(report_file)