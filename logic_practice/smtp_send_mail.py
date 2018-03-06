# -*- coding:utf-8 -*-
'''
@author:oldwai
'''
# email: frankandrew@163.com

import smtplib
from email.mime.text import MIMEText

send_mail = "457815031@qq.com"
recive_mail = "xiguanoldwai@163.com"
password = "0526oldwai"
message ="python 发送邮件测试"
host = 'smtp.163.com'  # 设置发件服务器地址
port = 25  # 设置发件服务器端口号。注意，这里有SSL和非SSL两种形式
sender = 'XXXXXX@163.com'  # 设置发件邮箱，一定要自己注册的邮箱
pwd = 'XXXXXX'  # 设置发件邮箱的密码，等会登陆会用到
receiver = 'XXXXXXXX@YY.com' # 设置邮件接收人，可以是扣扣邮箱
body = '<h1>Hi</h1><p>python 发送邮件测试</p>' # 设置邮件正文，这里是支持HTML的
msg = MIMEText(body, 'html') # 设置正文为符合邮件格式的HTML内容
msg['subject'] = 'Hello world' # 设置邮件标题
msg['from'] = recive_mail  # 设置发送人
msg['to'] = recive_mail  # 设置接收人

smtp = smtplib.SMTP(host, port)
smtp.login(recive_mail, password)
smtp.sendmail(recive_mail, recive_mail, msg=message.encode())
smtp.quit()
