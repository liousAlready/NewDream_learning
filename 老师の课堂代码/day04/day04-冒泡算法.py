'''
@File : day04-冒泡算法.py
@Time : 2021/4/11 14:35
@Author: luoman
'''
# import lib
# 冒泡算法：主要是要将序列进行排序；
# sort()
list02 = [10, 9, 5, 7, 3, 1]
# 第一轮： 9，5，7，3，1，10   找到最大的数 10
# 第二轮： 5，7，3，1，9，10   找到了第二大的数 9
# 第三轮： 5，3，1，7，9，10   找到了第三大的数 7
# 第四轮： 3，1，5，7，9，10   找到了第四大的数 5
# 第五轮： 1，3，5，7，9，10   找到了第五大的数 3
for i in range(0, len(list02)-1, 1):
    if list02[i] > list02[i+1]:
        list02[i], list02[i+1] = list02[i+1], list02[i]
print(list02)

for i in range(0, len(list02)-1, 1):
    if list02[i] > list02[i+1]:
        list02[i], list02[i+1] = list02[i+1], list02[i]
print(list02)

for i in range(0, len(list02)-1, 1):
    if list02[i] > list02[i+1]:
        list02[i], list02[i+1] = list02[i+1], list02[i]
print(list02)

for i in range(0, len(list02)-1, 1):
    if list02[i] > list02[i+1]:
        list02[i], list02[i+1] = list02[i+1], list02[i]
print(list02)

for i in range(0, len(list02)-1, 1):
    if list02[i] > list02[i+1]:
        list02[i], list02[i+1] = list02[i+1], list02[i]
print(list02)

print('=====改进成循环======')
for j in range(0, len(list02)-1, 1):
    for i in range(0, len(list02) - j-1, 1):
        if list02[i] > list02[i + 1]:
            list02[i], list02[i + 1] = list02[i + 1], list02[i]
print(list02)

# for和while循环如何选择：当明确知道循环的次数--for,当只知道循环结束的条件时---while

