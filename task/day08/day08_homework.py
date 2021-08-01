#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day08_homework.py
@time: 2021/5/10 11:04
'''

import xlrd
import xlwt
import smtplib  # 用来发邮件
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart  # 邮件中添加附件
from 老师の课堂代码.day08.day08_logger import Logging

'''
使用python代码从excel中获取五个学生的信息，生成五个学生对象；在控制台输出；
要求：
1、所有的代码需要使用类进行封装；
2、要求要使用异常处理：比如读取excel文件中的内容
3、要求使用日志模块，每一个函数中至少有一个日志打印
4、如果所有代码执行完成，使用邮件发送结果


# def readfile():
#     # 遍历
#     nrows = sheet_conent1.nrows
#     for i in range(nrows):
#         print(sheet_conent1.row_values(i))
'''

filename = "../day08/student.xlsx"
fajianren = "1650503480@qq.com"
shoujianren = ['1650503480@qq.com']
log = Logging().getloger()


class OpenFiles():

    def __init__(self, filename, filenubmer, fajianren, shoujianren):
        self.filename = filename
        self.filenubmer = filenubmer
        self.fajianren = fajianren
        self.shoujianren = shoujianren

    def read_excel(self, filename, filenubmer):
        # 打开文件
        wooker = xlrd.open_workbook(filename)
        try:
            # # 1.获取sheet的名字
            # listNames = wooker.sheet_names()
            # print(listNames)
            # # 1.2.按照索引号获取sheet的名字
            # shee1Names = wooker.sheet_names()[0]
            # print(shee1Names)
            # 2.获取sheet内容
            log.info("获取到文件，正在打开...")
            sheet_conent1 = wooker.sheet_by_index(filenubmer)
            # # 3.获取sheet的名称，行数，列数
            # print(sheet_conent1.name,sheet_conent1.nrows,sheet_conent1.ncols)
            #
            # # 4.查看某一行的数据
            # print(sheet_conent1.row_values(1))
        except Exception:
            print("当前的表不可用")
            log.error("坏了")
            log.info("坏了呀")
        else:
            return sheet_conent1

    def putemail(self, fajianren, shoujianren):
        self.fajianren = fajianren
        self.shoujianren = shoujianren
        # 先写头部
        sender = fajianren  # 发件人
        receviers = shoujianren  # 收件人

        # message = MIMEText("李守武给你一拳", "plain", 'utf-8')  # 邮件正文内容
        # 创建带附件的邮件
        message = MIMEMultipart()
        message['from'] = Header("李守武给你发来贺电", 'utf-8')
        message['To'] = Header("", 'utf-8')

        # 邮件的正文
        message.attach(MIMEText("查询结果成功！恭喜您！", "plain", 'utf-8'))

        subject = '等会儿我就直接就给你一拳！'
        message["Subject"] = Header(subject, 'utf-8')

        try:
            smtp = smtplib.SMTP("smtp.qq.com")  # 邮件服务器是谁

            smtp.login(fajianren, "uvrtyodtlkomcfdd")  # 用户名跟授权码

            smtp.sendmail(sender, receviers, message.as_string())
        except Exception:
            print("邮件发送失败")

    def readfile(self):
        cnt = 0
        sheet_conent1 = self.read_excel(self.filename, self.filenubmer)
        # 遍历
        try:
            nrows = sheet_conent1.nrows
            for i in range(nrows):
                # print(sheet_conent1.row_values(i)) # 取出数据为列表
                for c in sheet_conent1.row_values(i):  # 遍历列表，取出数据
                    # 让每5个就换行
                    cnt += 1
                    if cnt == 5:
                        cnt = 0
                    print(c, end="         " if cnt != 0 else "\n")  # 三目运算符
        except Exception:
            print("当前内容好像已丢失，请重新检查！！！")
            log.error("错误错误❎！")
        else:
            print("正在发送邮件！")
            log.info("正在发送邮件...")
            self.putemail(self.fajianren, self.shoujianren)  # 运行成功发送邮件


c = OpenFiles(filename, 0, fajianren, shoujianren)
c.readfile()
