#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day04_函数的嵌套.py
@time: 2021/4/19 21:21
'''


# 函数的嵌套 -- 分为 函数的嵌套定义 和 函数的嵌套调用
# 嵌套：一个函数中包含了另一个函数
# 嵌套定义：定义一个函数的时候，在其内部定义了另一个函数
def f1():
    print("hello f1")

    def f2():  # 函数只是定义，而不进行调用（使用）是没有任何效果
        print("hello f2")

    f2()  # 在函数中定义 在函数中调用，跟print平行


f1()


# f2() 错误方式


# 函数的嵌套调用：调用一个函数的时候，发现函数中调用另一个函数
def m1(a, b):
    if a > b:  # a if a>b else b
        return a
    else:
        return b


# 四个数比大小
def m2(a, b, c, d):
    result = m1(a, b)
    result = m1(result, c)
    result = m1(result, d)
    return result


print(m2(3, 4, 5, 6))
