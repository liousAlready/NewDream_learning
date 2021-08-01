#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day04_函数.py
@time: 2021/4/13 15:50
'''

''''
定义函数的语法：
def function(params):
    block
return expression/value

数学函数：
f(x)=2X+1

'''


def function(x):
    s = 2 * x + 1
    return s  # 可以改写成 ：return 2*x+1


def function1(x):
    return 2 * x + 1


# 函数定义完成后，必须要进行调用才能实现其功能
# 假设 x = 3
c = function(3)
print("函数的运行结果是：", c)
b = function1(9)
print("函数的运行结果是：", b)

'''
假设定义数学函数：
f(x,y)= x*y + 2*x + 1  二元一次函数

f(2,4)= 2*4 + 2*2 + 1 = 13

'''


def f(x, y):
    return x * y + 2 * x + 1


dd = f(2, 4)
print("dd 的结果是", dd)


# 多个条件使用
def f2(x, y, z):
    return x + y + z + 10


ee = f2(3, 4, 5)
print("ee 的结果是", ee)


# python中是可以存在没有参数和没有返回值的函数的
def f3():
    print("$")


f3()


# 可能是有参数但是没有返回值
def f4(n):
    print("$" * n)


f4(3)


def f5(n):
    return "$" * n


f = f5(5)
print("f5的运行结果是：", f)

# 把定义函数的使用的参数称之为 形式参数--形参
# 把调用函数的时候使用的具体指成为 实际参数--实参

# 参数传递：传数值 传地址
# 可变的数据类型：列表、字典
# 不可变的数据类型：数据类型、字符串、元祖、集合 --传数值
a = 10
b = 5


def f6(a, b):
    a = a + b
    return a


print("a的值是", a)

list01 = ['nn', 'java']


def f6(list,s):
    list.append(s)

f6(list01,"hello")
print(list01)