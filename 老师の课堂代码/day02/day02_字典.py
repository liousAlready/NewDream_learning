'''
@File : day02_字典.py
@Time : 2021/3/31 20:14
@Author: luoman
'''
# import lib
# 汉字---对应名词解释 字典数据类型---键值对(key-value)的方式存储
# 功能：联系人 人名--手机号   昵称--QQ号
# 字典的定义 dict()  {}
# key(键名)是不允许重复 value(值)是可以重复的
dict1 = {}  # 空字典
# 方法一：
dict2 = {'x': 1, 'y': 2}
# 方法二：
dict3 = dict(x=1, y=2)
# 方法三：
dict4 = dict((['x', 1], ['y', 2]))
print('字典2', dict2)
print('字典3', dict3)
print('字典4', dict4)

# 可以在定义的时候，不同的key 对应同一个值
# fromkey(s,v)  s的元素是可以做为键名   v的元素可以做为值
list1=['x', 'y', 'z']
dict5 = dict.fromkeys(list1, 'x')
dict6 = {}.fromkeys(list1, ['x', 8])
print(dict5)
print(dict6)
# 更新字典 dict2
dict2['y'] = 3
print('更新后的dict2', dict2)
# 如果key名不存在于字典中，则会把这一个key和value添加到字典中
dict2['z'] = 4
print('更新后的dict2', dict2)
# 比如：在原来的dict2的y值上进行+5
dict2['y'] = dict2['y'] + 5
print(dict2)
# 删除字典和删除字典中的一个键值对
# del dict6
# del dict6['y']
# print(dict6)

# 字典的处理函数
# 1、adict.keys() 返回一个包含字典所有KEY的列表；
print(dict3.keys())
# 2、adict.values() 返回一个包含字典所有value的列表；
print(dict3.values())
# 3、adict.clear() 删除字典中的所有项或元素；
dict2.clear()
print(dict2)
# 4、adict.get(key, default = None) 返回字典中key对应的值，若key不存在字典中，则返回default的值（default默认为None）；
print('字典3中的x的值:', dict3.get('x'))
print('字典3中的n的值:', dict3.get('n'))

# 5、adict.pop(key[,default]) 和get方法相似。如果字典中存在key，删除并返回key对应的vuale；如果key不存在，且没有给出default的值，则引发keyerror异常；
print('删除字典3中x', dict3.pop('x'))
print(dict3)
print('删除字典3中t:', dict3.pop('t', '键不存在'))
print(dict3)
# 6、adict.update(bdict) 将字典bdict的键值对添加到字典adict中，无则添加，有则覆盖
dict7 = {'x': 4, 't': 6, 'y': 7}
# 把dict7 添加到dict3
dict3.update(dict7)
print(dict3)




