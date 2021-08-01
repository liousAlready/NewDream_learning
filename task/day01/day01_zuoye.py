#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day01_zuoye.py
@time: 2021/3/28 18:33
'''

# 1、有一个字符串“abcdefgh” 编写代码显示“cdefgh”  "gh"
str1 = 'abcdefgh'
print(str1[2:])
print(str1[-2:])
print(str1[6:8])

# 2、有一个字符串“12345678”，进行切片[:-3]  [2:6]  [-2:]分别是多少
str2 = '12345678'
print(str2[:-3])  # 12345
print(str2[2:6])  # 3456
print(str2[-2:])  # 78

'''
3、定义列表：
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]  
'''
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 请分别取出['Apple', 'Google', 'Microsoft’]、’Ruby’,[‘Adam’,’Bart’]
print(L[0])  # 取出['Apple', 'Google', 'Microsoft’]
strs = L[1][2]  # 取出 Ruby
strs1 = L[1][2:3]  # 取出 ['Ruby']
strs2 = L[2][0:2]  # 取出 [‘Adam’,’Bart’]
print(strs)
print(strs1)
print(strs1 + strs2)  # 取出 'Ruby',[‘Adam’,’Bart’]

# 计算列表长度并输出
print(len(L))
# 列表中追加元素"seven"，并输出添加后的列表
L.append(['seven'])
print(L)
# 请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表
L.insert(0, 'Tony')
print(L)
# 请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
L[1] = ["Keylly"]
print(L)

# 4.写代码，有如下列表，按照要求实现每一个功能：
li = ['alex', 'eric', 'rain']
# 4.1 计算列表长度并输出
print(len(li))
# 4.2 列表中追加元素"seven"，并输出添加后的列表
li.append('seven')
print(li)
# 4.3 请在列表的第1个位置插入元素 "Tony"，并输出添加后的列表 
li.insert(0, "Tony")
print(li)
# 4.4 请修改列表第2个位置的元素为 "Kelly"，并输出修改后的列表
li[1] = "kelly"
print(li)
# 4.5 请删除列表中的元素"eric"，并输出修改后的列表
li.remove("eric")
# li.pop(2) # 采用pop定位位置
print(li)
# 4.6 请删除列表中的第2个元素，并输出删除的元素的值和删除元素后的列表
print(li.pop(1))
print(li)
# 4.7 请删除列表中的第3个元素，并输出删除元素后的列表
li.pop(2)
print(li)
# 4.8 请删除列表中的第2至4个元素，并输出删除元素后的列表
li = ['Tony', 'kelly', 'eric', 'rain', 'seven', 'newnumber']
print("原列表为：", li)
li[2:5] = []
print("删除后的列表为", li)

'''
百度：
# 切片的本意为截取原有列表中指定的的某一段，或者说是复制指定的那一段，并返回了新的列表
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("原列表为：", lst)
# 借助列表的添加方式，原来添加的操作中，使得lst[start,stop] = lst1（此为添加的元素）
# 那么删除操作可以类似的，使lst1为空列表，那么原列表中指定一段的元素被空替代，则完成删除
lst[1:3] = [] # 将第1,2索引位的元素删除
print("删除后的列表为：", lst)
'''

# 4.9 请将列表所有的元素反转，并输出反转后的列表
li.reverse()
print(li)

print(li[::-1])