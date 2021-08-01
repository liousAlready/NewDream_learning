#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day08_异常处理.py
@time: 2021/5/9 11:28
'''

# 异常：与错误区别  exception   error
# 为什么要处理异常：希望程序在出现问题是，仍然能够继续运行
# for i in range(1, 4):
#
#     try:
#         a = int(input())
#         b = int(input())
#         c = a // b
#     except ValueError:
#         print("数据类型出错！")
#     except ZeroDivisionError:
#         print("除数不能为0")
#     else:
#         print(c)


# for i in range(1, 4):
#     try:
#         a = int(input())
#         b = int(input())
#         c = a // b
#     except Exception:  # 异常的父类
#         print("hahaha")
#     else:
#         print(c)

# 捕捉异常可以使用try/except语句
'''
形式一：
try:
    可能会出现异常的语句
excepe:
    异常处理语句
else:
    没有出现异常的时候执行
    
形式二：
try:
    可能会出现异常的语句
excepe:
    异常处理语句
finally:
    不管是否出现异常，都会执行

'''

# for i in range(1, 4):
#
#     try:
#         a = int(input())
#         b = int(input())
#         c = a // b
#     except Exception:
#         print("除数不能为0")
#     finally:
#         print("打印结果", c)


''''
触发异常：
        python中的 raise 关键字用于引发一个异常，语法格式如下：
        raise [Exception [, args[,tarceback]]]
        
'''
level = None


def scorelevel(score):
    global level
    if 0 <= score < 60:
        level = "C"
        return ("C")
    elif 60 <= score <= 80:
        level = "B"
        return ("B")
    elif 81 <= score <= 100:
        level = "A"
        return ("A")
    else:
        raise Exception("Invalid score")


try:
    scorelevel(101)
except Exception as err:
    print("请输入0-100之前的成绩", err)
else:
    print(level)
