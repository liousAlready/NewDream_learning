#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: 讲解.py
@time: 2021/4/7 20:10
'''

import ast

'''
1、建一个列表list01 , 列表中的值通过 input函数输入 ，然后打印整个列表
2、有一个列表[1,2,3,40.5,6],把其中的小数转为整型输出
3、定义字符串列表，在列表中存入你喜欢的5首歌。请输出你最喜欢的歌名及他所在的位置。
4、定义字符串列表，把你喜欢的5个名星名字添加在列表中，把你最不喜欢的人名输出，修改第三号位置的人名。
5、有字典 dic = {"k1": "v1", "k2": "v2", "k3": "v3"}，实现以下功能：
   5.1 输出字典中所有的key
   5.2 输出字典中所有的value
   5.3  添加一个键值对"k4","v4",输出添加后的字典 dic
   5.4  删除字典 dic 中的键值对"k1","v1",并输出删除后的字典 dic
   5.5 删除字典 dic 中 'k5' 对应的值，若不存在，使其不报错，并返回None
   5.6 获取字典 dic 中“k2”对应的值
   5.7 有字典 dic2 = {'k1':"v111",'a':"b"} 通过一行操作使 dic2 = {'k1':"v111",'k2':"v2",'k3':"v3",'k4': 'v4','a':"b"}
6：现有列表如下：
list = [['k', ['qwe', 20, {'k1': ['tt', 3, '1']}, 89], 'ab']]
6.1 将列表中的‘tt’变成大写
6.2  获取列表中的 k1对应的值
'''

#  1、建一个列表list01 , 列表中的值通过 input函数输入 ，然后打印整个列表
# input 输入的数据都是字符串
# list01 = []
# a = input()
# b = input()
# c = input()
# list01.append(a)
# list01.append(b)
# list01.append(c)
# print(list01)
#
# # 方法二
# list02 = list(ast.literal_eval(input("请输入值：")))
# print(list02)
# # literal_eval() 作用是：把python的字符串中的数据转换成对应的数据格式


# 2、有一个列表[1,2,3,40.5,6],把其中的小数转为整型输出
list03 = [1, 2, 3, 40.5, 6]
# 索引
list03[3] = int(list03[3])
print(list03)

list04 = [1, 2, 3, 40.5, 6]
# 方法二： for
for i in list04:
    if type(i) == float:
        print(int(i))

# 方法三：instanse（）
for i in list04:
    if isinstance(i, float):
        print(int(i))
# isinstance 是专门判断数据类型的函数
# isinstance （值，数据类型）

