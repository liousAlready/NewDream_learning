#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day05_文件的处理03.py
@time: 2021/4/18 15:26
'''

import os

# 如果是windows操作系统，如果写文件的路径用\，一定要写双斜杠，如果写/，只要一个/


oldname = 'file/今晚打老虎.txt'
newname = 'file/p9.txt'
# # 修改文件的名字
# #os.rename(oldname,newname)
#
# # 删除文件名字
# os.remove(newname)

# 1.创建文件夹
filename = "p9"
# 2.判断文件或者文件夹是否已经存在
if os.path.isdir(filename):
    print("文件夹已经存在了")
else:
    os.mkdir(filename)
# 判断文件夹是否存在
if os.path.isfile(oldname):
    print("文件已经存在")
else:
    pass

# 3.删除文件夹--只能删除空文件夹
# os.rmdir(filename)
# 4.切换目录
# if os.path.isdir(filename):
#     os.chdir(filename)
#   os.mkdir("p9_A")

# 5.删除非空目录
# 先要删除目录中的文件，再删除目录

# 6.创建多级目录
# if os.path.isdir(filename):
#      os.makedirs(filename + '/p9_B/P9_bb')

# 获取当前操作目录的路径
print(os.getcwd())
# 一般会这样写
# os.getcwd() + "logs"

# 获取当前路径的绝对路径
print(os.path.abspath(os.getcwd()))
# 获取当前路径的相对路径
print(os.path.realpath(os.getcwd()))
