'''
@File : day05-excel文件的处理.py
@Time : 2021/4/18 16:46
@Author: luoman
'''
# import lib
import xlrd
import os
# 处理excel(.xlsx)
# xlrd  模块处理excel文件
# 安装,在dos命令窗口: pip install xlrd

# 创建excel文件
filename = '../file/stu.xls'
workbook = xlrd.open_workbook(filename,formatting_info=True,encoding_override="utf-8")
# excel 处理  csv处理
