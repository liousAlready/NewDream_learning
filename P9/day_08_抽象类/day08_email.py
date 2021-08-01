#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day08_email.py
@time: 2021/5/9 15:01
'''

# stmp pop3 imap
# smtp email
# 邮件的构成部分： 发件人 收件人 标题 正文 附件
import smtplib  # 用来发邮件
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart  # 邮件中添加附件


def putemail():
    # 先写头部
    sender = "1650503480@qq.com"  # 发件人
    receviers = ['1650503480@qq.com']  # 收件人

    # message = MIMEText("李守武给你一拳", "plain", 'utf-8')  # 邮件正文内容
    # 创建带附件的邮件
    message = MIMEMultipart()
    message['from'] = Header("python测试", 'utf-8')
    message['To'] = Header("1650503480", 'utf-8')

    # 邮件的正文
    message.attach(MIMEText("李守武给你一拳", "plain", 'utf-8'))
    # 添加附件

    fujian = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    # 设置附件在收件方的显示
    fujian['Content-Type'] = 'application/octet-stream'
    fujian['Content-Disposition'] = 'attachment;filename="student.txt"'
    message.attach(fujian)

    subject = '我直接就给你一拳！'
    message["Subject"] = Header(subject, 'utf-8')

    try:
        smtp = smtplib.SMTP("smtp.qq.com")  # 邮件服务器是谁

        smtp.login("1650503480@qq.com", "uvrtyodtlkomcfdd")  # 用户名跟授权码

        smtp.sendmail(sender, receviers, message.as_string())
    except Exception:
        print("邮件发送失败")


file_name = '../../file/hello.txt'
putemail()
