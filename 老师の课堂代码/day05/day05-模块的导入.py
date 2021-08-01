'''
@File : day04-模块的导入.py
@Time : 2021/4/18 11:33
@Author: luoman
'''
# import lib
# 什么是模块---把一个py文件就称之为一个模块
# 为了方便为护代码，会把不同功能的函数写到不同的py文件中
# 如果此时a模块想用b模块中的函数，该如何操作

def add(a,b,c):
    return a + b + c

# 查看系统内置模块
# print(help('modules'))
# pip 功能是用来安装第三方模块----是由其它公司开发  selenium   在线安装
# pip 工具在 python安装目录下的scripts文件下 pip.exe
# 如何执行: 在dos命令窗口下输入 pip install 模块名  ---python环境变量

# 如何导入系统模块   import 模块名
import time
import os
import sys

from demo import day05_函数的递归 as dd  # 给模块取别名

dd.story()

# 导入后：模块名.函数名









