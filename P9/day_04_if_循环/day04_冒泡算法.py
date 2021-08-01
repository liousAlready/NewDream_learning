#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day04_冒泡算法.py
@time: 2021/4/13 14:54
'''

# 冒泡算法: 主要是将序列进行排序
# sort()  数据量大时数据响应慢

list02 = [10, 9, 5, 7, 3, 1]
# 第一轮: 9,5,7,3,1,10 找到最大的数 10
# 第二轮：5,7,3,1,9,10 找到第二大的数 9
# 第三轮: 5,3,1,7,9,10 找到第三大的数 7
# 第四轮: 3,1,5,7,9,10 找到第四大的数 5
# 第五轮: 1,3,5,7,9,10 找到第五大的数 3
for i in range(0, len(list02) - 1, 1):
    if list02[i] > list02[i + 1]:
        list02[i], list02[i + 1] = list02[i + 1], list02[i]
print(list02)

for i in range(0, len(list02) - 1, 1):
    if list02[i] > list02[i + 1]:
        list02[i], list02[i + 1] = list02[i + 1], list02[i]
print(list02)
for i in range(0, len(list02) - 1, 1):
    if list02[i] > list02[i + 1]:
        list02[i], list02[i + 1] = list02[i + 1], list02[i]
print(list02)

for i in range(0, len(list02) - 1, 1):
    if list02[i] > list02[i + 1]:
        list02[i], list02[i + 1] = list02[i + 1], list02[i]
print(list02)

for i in range(0, len(list02) - 1, 1):
    if list02[i] > list02[i + 1]:
        list02[i], list02[i + 1] = list02[i + 1], list02[i]
print(list02)

for i in range(0, len(list02) - 1, 1):
    if list02[i] > list02[i + 1]:
        list02[i], list02[i + 1] = list02[i + 1], list02[i]
print(list02)

print("======冒泡改进成循环======")
for j in range(0, len(list02) - 1, 1):
    for i in range(0, len(list02) - j - 1, 1):
        if list02[i] > list02[i + 1]:
            list02[i], list02[i + 1] = list02[i + 1], list02[i]

print(list02)
