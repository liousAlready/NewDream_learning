#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day01_6_元组和集合.py
@time: 2021/3/28 16:52
'''

# 元祖 tuple 定义元祖使用()  元组是不可变的列表
tuple1 = (2, 3, 4, 5)
tuple2 = ('hello', 'world')
print(tuple1)
# tuple1.append(6) 错误操作 print(tuple1)

# 拼接 重复 切片 索引 与列表、字符串相同
print(tuple1 + tuple2)
print(tuple1 * 4)
print(tuple1[1])
print(tuple1[1:4])

# 告诉元素所在位置 index
print(tuple1.index(4))
# 统计元素出现的次数
print(tuple1.count(5))

# 注意事项：定义的元组 如果只有一个元素的话 那么需要在元素后面加逗号（,)
tuple3 = (3,)
print(tuple3)

# 集合 set 定义 set() 定义空集合
# 特点：无序，不重复  集合中的数据 并不关心数据的位置问题
set1 = {}  # 空集合为类型为字典
print(type(set1))
# 定义空集合
set1 = set()
print(type(set1))

set2 = {2, 2, 2, 2, 2}  # 不重复
print(set2)

set3 = {'f', 'e', 'c', 'ce'}
set4 = {'b', 'a', 'c', 'ce'}

print(set3)
# 集合进行运算
#  | 并集运算
print(set2 | set3)
#  - 差集运算
print(set3 - set4)  # 只求出set3中与set4中不同的数据，set中异常的数据不显示
#  & 交集运算  元素中一样的元素
print(set3 & set4)
# ^ 求两个集合中互不存在的元素
print(set3 ^ set4)

# in 使in可以判断某个元素是否存在于 列表 元素 集合
print('cc' in set4)  # 如果是，返回True  如果不是 返回False
