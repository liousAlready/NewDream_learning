#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day08_excel表的数据读写.py
@time: 2021/5/9 14:17
'''

# excel 的后缀有两个 xls喝xlsx
# xlrd 读取excel表中的数据
# xlwt

import xlrd

# 第一步 创建工作簿对象
workbook = xlrd.open_workbook('/P9/file/Car.xlsx')
# 第二步 创建表对象
# 方法一： 通过表的名字来创建
sheet = workbook.sheet_by_name("Sheet1")
# 方法二： 通过表的索引来创建表对象
#sheet = workbook.sheet_by_index(0) # 索引的下表是从0开始的


# 操作表
# 1.查看表中的数据有多少行
print(sheet.nrows)
# 2.查看某一行数据
print(sheet.row(1))