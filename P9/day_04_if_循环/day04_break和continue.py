#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day04_break和continue.py
@time: 2021/4/13 13:47
'''

# # break 和 continue
# # break：破坏，跳出本层循环
# # continue： 继续，结束本次循环，继续下一次循环
# i = 1
# while i <= 10:
#     if i == 5:
#         break
#     print(i, end="\t")
#     i = i + 1
# print("结束")
#
# i = 1
# while i <= 10:
#     i = i + 1
#     if i == 5:
#         continue
#     print(i, end="\t")
# #   i = i + 1  # i放在这儿不会进行自增，所以需要把i放到最上方
# print("结束")
#
# print("=========当j=5的时候 break=============")
# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         if j == 5:
#             break  # 跳出循环 到五结束 最多打印到第四个
#         print("%d * %d = %d" % (j, i, i * j), end='\t')
#         j = j + 1
#     print()
#     i = i + 1
#
# print("======================")
# n = 1
# while True:
#     n = n + 1
#     if n == 4:
#         break
#     print(n)

# 举例 ： 如果用户输入0 表示程序结束，如果输入1表示：登录，输入2表示：注册，输入3表示：查询
while True:
    start = int(input("请输入你要进行的操作: \t"))

    if start == 0:
        print("程序结束")
        break
    elif start == 1:
        print("登陆")
    elif start == 2:
        print("注册")
    elif start == 3:
        print("查询")
    else:
        print("输入报错了！")
