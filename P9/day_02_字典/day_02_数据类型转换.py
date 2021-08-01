#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day_02_数据类型转换.py
@time: 2021/3/31 20:54
'''

# 类型转换
# 分为两种： 自动转换  强制转换
# 自动转换：发生在数值类型 bool+int+float--float
a = 10
b = True
print(a + b)

c = 3.4
print(a + b + c)

# 强制转换
print('强制转换成int：', int(a + c))
print('强制转换成int：', int(c))
print('强制转换成int：', float(a))
set1 = {1, 2, 3}
print('强制转换成list:', list(set1))
print('转换成字符串', repr(set1))  # 字符串
print('转换成字符串', str(set1))
str1 = '1+2'  # eval 将字符串中有效表达式提取出来并进行计算  1+2 =3
print(eval(str1))

n = '中'
# 十六进制
print('十六进制的形式： %x' % ord(n))  # ord把字符转换成对应的整数

tuple1 = (('x', 1), ('y', 2))  # 将元组转换成字典
print(dict(tuple1))
