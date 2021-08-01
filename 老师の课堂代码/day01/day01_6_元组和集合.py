'''
@File : day01_6_元组和集合.py
@Time : 2021/3/28 16:52
@Author: luoman
'''
# import lib
# 元组  tuple 定义元组使用 () 元组是不可变的列表
tuple1 = (2, 3, 4, 5)
tuple2 = ('hello', 'world')
print(tuple1)
# tuple1.append(6) 错误操作
# print(tuple1)
# 拼接 重复  切片 索引  与列表相同
print(tuple1 + tuple2)
print(tuple1 * 4)
print(tuple1[1:3])
# 告诉元素所在的位置 index()
print(tuple1.index(4))
# 统计元素出现的个数 count()
print(tuple1.count(5))
# 注意事项 定义的元组如果只有一个元素的话，那么需要在元素后加一个,号
tuple3 = ('python',)
print(tuple3)

# 集合 set 定义 set()定义空集合  {}
# 特点：无序，不重复  集合中的数据 并不关心数据的位置
# set1 = {} # 定义的是一个空字典
# 定义空集合
set1 = set()
print(set1)
print(type(set1))
set2 = {2, 2, 2, 2, 2}
print(set2)
set3 = {'aaa', 'bbb', 'cc', 'fff'}
set4 = {'aaa', 'bbb', 'eee', 'ddd'}
print(set3)
# 进行运算
# | 并集运算
print(set2 | set3)
# - 差集运算
print(set3 - set4) # 只求出set3中与set4中不相同的数据，set4中异常的数据不显示

# & 交集运算
print(set3 & set4)

# ^ 求两个集合中互不存在的元素
print(set3 ^ set4)

# in 使in可以判断某个元素是否存在于列表 元组 和 集合
print('cc' in set4)  # 如果是，返回True  如果不是 返回 False
print('cc' in set3)

