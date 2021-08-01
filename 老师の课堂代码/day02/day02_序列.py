'''
@File : day02_序列.py
@Time : 2021/3/31 21:12
@Author: luoman
'''
# import lib
# 序列：字符串，列表，元组
'''
len()：求序列的长度              +：连接两个序列
*：重复序列元素                 in：判断元素是否在序列中
max()：返回序列最大值         min()：返回序列最小值
'''

str1 = 'hello'
list3 = [3, 5, 2, 9, 10, 56]
print('序列的长度：', len(str1), len(list3))
print(max(list3))
print(min(list3))
#  in：判断元素是否在序列中 如果存在 返回值 True  反之为 False
print('e' in str1)
print('e' in list3)

# Python输入输出语句
# 输入语句 input(): 从键盘中接收数据到变量中； input()接收到的数据都当做字符串处理
# name = input()
# print('name为', name)
# print('name的类型为:', type(name))
#
# #age = int(input())
# #age = int(input('起提示作用'))
# print('age:', age, type(age))
# 输出
# print() 默认是使用 换行符结尾 \n

print('hello', end='：')
print('大家好')
print()# 换空行
print('您 好')
print(str1, list3)
# 格式化输出 % 标记
# str.format()
name = 'll'
age = 19
print('{}的年龄是{}岁'.format(name, age))

print('{0}的年龄是{1}岁'.format(name, age))

print('{n}的年龄是{a}岁'.format(n=name, a=age))








