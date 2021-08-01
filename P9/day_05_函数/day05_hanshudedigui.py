#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day05_hanshudedigui.py
@time: 2021/4/18 11:07
'''

# 通过循环进行1--100的假发运算
sum = 0
for i in range(1, 101):
    sum = sum + i
print(sum)


# 改进成递归
def add(n):
    if n == 1:
        return 1
    else:
        return add(n - 1) + n


s = add(100)
print(s)


# 匿名函数：函数的定义不需要写 def 关键字， 也不需要return 关键字：lambda
# 有些函数的功能只有一句话就可以进行实现
def add(a, b):
    return a + b


# 转换成匿名函数
# 此时的冒号前的a,b 就是函数的形式参数，sum既可以保存函数的运行结果
# 也可以当做函数的名字
sum = lambda a, b: a + b
print(sum(1, 3))

#  使用匿名函数来比较两个数的大小
m = lambda: 4 if 4 > 5 else 5
print(m())


# 内置函数--有些函数是由系统定义好的

# 定义函数的时候：1、除特殊情况外，自定义函数中不写input语句和print语句
#              2、定义函数时，要注意函数的名字不能与内置函数相同

# def add():  # 错误示范
#     a = int(input())
#     b = int(input())
#     return a+b
# print(add())

def add(a, b):
    return a + b


print(add(1, 3))
