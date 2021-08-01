#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day05_文件的处理类型04_excel.py
@time: 2021/4/18 16:47
'''

# 处理excel文件(.xlsx)  2007以后的版本

# xlrd 模块处理excel文件
import xlrd
import os

# 处理excel(.xlsx)
# 创建excel文件

workbook = xlrd.open_workbook(r'file/stu1.xls')

# 获取所有sheet
sheet_name = workbook.sheet_names()[0]

# 根据sheet索引或者名称获取sheet内容
sheet = workbook.sheet_by_index(0)  # sheet索引从0开始
print(sheet.name, sheet.nrows, sheet.ncols)
