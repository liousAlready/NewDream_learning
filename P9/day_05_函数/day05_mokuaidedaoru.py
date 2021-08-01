#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day05_mokuaidedaoru.py
@time: 2021/4/18 11:33
'''


# 什么是模块  --把一个py文件就称之为一个模块
# 为了方便维护代码，会把不同功能的函数写到不同的py文件中
# 如果此时a模块想用b模块中的函数，该如何操作
# def add(a, b, c):
#     return a + b + c


# 查看系统内置模块
print(help('modules'))

# pip 安装第三方模块--由第三方公司开发的工具
# pip 工具在pyton安装目录下的scripts文件下的 pip.exe文件
# 如何执行：dos命令窗口下输入 pip_install 模块名

# 如何导入系统模块
from P9.day_05_函数 import day05_hanshudedigui as b
c = b.add(3,4)
print(c)