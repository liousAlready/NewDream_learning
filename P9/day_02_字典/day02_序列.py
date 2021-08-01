#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day02_序列.py
@time: 2021/3/31 21:13
'''

# 序列：字符串、列表、元组 统称为序列

'''
常见序列操作：
len()：求序列的长度  +：连接两个序列  *：重复序列元素
in：判断元素是否在序列中 max()：返回序列最大值 min()：返回序列最小值
'''

str1 = 'hello'
list3 = [3, 5, 15, 25, 11, 90]
print('序列长度', len(list3), len(str1))
# max() min()
print('列表中的最大值', max(list3), '列表中的最小值', min(list3))

# in 判断元素是否在序列中 如果存在 返回值 True 反之为Fasle
print('e' in str1)
print('e' in list3)

# # 输入输出语句  input() 函数接受到的数据都当做字符串处理
# book_name = input("请输入你需要的书籍：")
# print('借阅的书籍名称为', book_name)
#
# # 想要变成数字类型的数据
# age = int(input('你今年多大了？'))
# print('我今年 ', age, ' 岁了')

# 输出语句
print("hello", end='：')  # 改变换行 end
print('大家好啊')
print()  # 不输入信息 换空行
print("你 好")
print(list3, str1)
# 格式化输出  % 标记
# str.format()
name = 'lsw'
age = 19
print('{}的年龄是{}岁'.format(name, age))  # 格式化 {} 留位置给后面参数
print('{0}的年龄是{1}岁'.format(name, age))
print('{n}的年龄是{a}岁'.format(n=name, a=age))
