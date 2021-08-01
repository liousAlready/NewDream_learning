'''
@File : day08-email.py
@Time : 2021/5/9 15:00
@Author: luoman
'''
# import lib
# smtp email
# 邮件的构成部分：发送人 收件人  标题   正文  附件
import smtplib  # 用来发邮件
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
# 请在这里加上日志
from 老师の课堂代码.baidu_selenium_demo.comm.logger import log

def sendemail(filename):
    # 先写头部
    sender = '573379783@qq.com'
    receviers = ['573379783@qq.com']
    # 写纯文本的邮件
    # message = MIMEText('python基础课程内容测试','plain','utf-8')
    # 创建带附件的邮件
    message = MIMEMultipart()
    message['from'] = Header('python测试', 'utf-8')
    message['To'] = Header('573379783', 'utf-8')

    # 邮件的正文
    message.attach(MIMEText('百度首页测试报告','plain','utf-8'))
    # 添加附件,取出附件内容
    fujian = MIMEText(open(filename, 'r').read(),'base64','utf-8')
    # 设置附件在收件方的显示
    fujian['Content-Type']='application/octet-stream'
    fujian['Content-Disposition'] ='attachment;filename="stuinfo.txt"'
    message.attach(fujian)

    subject = '百度首页测试报告'

    message['Subject'] = Header(subject,'utf-8')

    try:
        smtp  = smtplib.SMTP('smtp.qq.com') # 邮件服务器是谁

        smtp.login('573379783@qq.com','*************')

        smtp.sendmail(sender,receviers,message.as_string())
        print('邮件发送成功')
    except Exception:
        print('邮件发送失败')







