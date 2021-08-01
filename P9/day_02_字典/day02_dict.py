#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day02_dict.py
@time: 2021/3/31 20:16
'''

# 字典是无序的  dict
# 汉字 -- 对应名词解释  字典数据类型-- （键 key--值对 value） 的方式存储
# 字典的使用范围：手机号码联系人  人名--手机号码  昵称--QQ号
# 字典的定义 dict() {"key":value}
# key(键名)是不允许重复 value(值)是可以重复的

dict1 = {}  # 空字典
# 定义字典 方法一
dict2 = {"x": 1, "y": 2}
print(dict2)
# 方法二
dict3 = dict(x=1, y=2)
print(dict3)
# 方法三
dict4 = dict((['x', 1], ['y', 2]))
print(dict4)

# 可以在定义的时候，不同的key，对应不同的值
# fromkey(s,v) s的元素是可做为键名 v的元素可以做为值
list1 = ['x', 'y', 'z']
dict5 = dict.fromkeys(list1, '9527')  # 9527做为值
# dict5 = {}.fromkeys(list1, '9527')  # 9527做为值
print(dict5)
# 值
dict6 = dict.fromkeys(list1, ['x', 8])
print(dict6)

# 更新字典 dict2
dict2['y'] = 3
print("更新之后的dict2", dict2)
# 如果key名不存在与de字典中，则会把这一个key和value添加到字典中来
dict2['z'] = 199
print("更新之后的dict2", dict2)
# 例子：在原来的dict2的y值上进行+5
dict2['y'] = dict2['y'] + 5
print(dict2)
print(dict6)

"""# 删除字典中的某一个键值
del dict6['y']
print(dict6)

# 删除字典
del dict6
print(dict6)"""

# 字典的处理函数
# 1、adict.keys()返回一个包括字典所有KEY的列表：
print(dict3.keys())
# 2、adict.values()返回一个包括字典所有Vaules的列表：
print(dict3.values())
# 3、adict.clear()删除字典中的所有项或元素：
dict2.clear()
print(dict2)
# 4、adict.get(key,default=None)返回字典中key对应的值，若key不存在字典中，则返回default的值（default默认为None）；
print("字典3中的x的值：", dict3.get('x'))
print("字典3中的n的值", dict3.get('n'))

# 5、adict.pop(key[,default])和get方法相似。如果字典中存在key，删除并返回key对应的vuale；如果key不存在，且没有给出default的值，则引发keyerror异常；
print('删除字典3中x', dict3.pop('x'))
print(dict3)
print('删除字典3中x', dict3.pop('t', '该键不存在'))  # 不存在的键 需要给一个默认的value
print(dict3)

# 6、adict.update(bdict)将字典bdict的键值对添加到字典adict中，无则添加，
dict7 = {'x': 4, 't': 6, 'y': 999}  # 若字典中存在该键 则会覆盖字典中存在的值
# 把字典7 添加到dict3
dict3.update(dict7)
print(dict3)


