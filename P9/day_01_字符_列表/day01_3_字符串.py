#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day01_3_字符串.py
@time: 2021/3/28 14:16
'''

# 定义字符串：需要使用引号： ' ''  三个引号都是可以的

str1 = '李嘶'
str2 = "李四"
str3 = '''ask'''
print(str1)

# 三个英豪 1、定义字符串 2、可以进行多行注释
#  注释 ： 以# 开头 进行单行注释

str4 = 'hello P9班的同学大家好：' \
       '大家上班辛苦了！！'

print(str4)

str5 = '''hello P9班的同学们大家好：
            今天长沙的太大很大，可以出去晒太阳'''

print(str5)

# 转义符  有一些特殊的字符是无法直接输出的，有特殊的含义。比如说换行符
print('\n')  # 换行符

# 字符串的索引 -- 顺序
# 从左往右进行索引排序：下标从0开始
str6 = 'python'
# 切一个字符
print(str6[0])  # 从左往右
print(str6[-1])  # 从右往左
# 切多个字符,就要有起始值和结束值：变量名[起始值：结束值]
print(str6[0:3])
# 如果要切刀字符串的结尾
print(str6[2:])
print(str6[-4:5])
print(str6[-4:-5])  # 错误写法

# 字符串可以进行 重复* 拼接 + （拼接：同类的想数据类型才能进行拼接）
print(str6 * 7)
print(str1 + str6)

# 字符串的处理函数
print(str6.capitalize())  # 将字符串的首字母大写
print(str6.upper())  # 将字符串都变为大写
print(str6.lower())  # 将字符串都变成小写
str7 = 'P9.py'
print(str7.split('.'))  # 分割字符串
str8 = '2020年'
# replace('x','y',1) 第一个原参数，第二个想要替换的参数，第三个替换次数
print(str8.replace('0', '1', 1))  # 替换字符串，没有起始，全局替换，可以选择替换次数


