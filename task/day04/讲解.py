#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: 讲解.py
@time: 2021/4/18 08:50
'''

# # 4、使用循环语句计算从1到100，一共有多少个尾数为7或者7的倍数这样的数，请输出这样的数。
# num = []  # 采用一个空列表
# for i in range(1, 101, 1):  # 循环列表
#     if i % 7 == 0:
#         num.append(i)
#     elif str(i)[-1] == '7':  # 取字符串最后一位字符来进行判断
#         num.append(i)
#
# print(num)
#
# # 讲解
# count = 0
# for i in range(1, 101, 1):
#     if i % 10 == 7 or i % 7 == 0:
#         print("i为：", i)
#         count = count + 1
#     else:
#         continue
# else:
#     print("总共是：", count)

# 5、模拟支付宝的蚂蚁森林通过日常的走步--20g，生活缴费--50g，线下支付--100g，网络购票--80g，共享单车--200g等低碳，环保行为可以积攒能量，当能量达到一定数量后，可以种一棵真正的树--500g。
# 5.1由用户输入环保行为，来积累能量；查询能量请输入能量来源！退出程序请输入0；

# e = [{"xingwei": "日常的走步", "nengliang": 20, "jilei": 0},
#      {"xingwei": "生活缴费", "nengliang": 50, "jilei": 1},
#      {"xingwei": "线下支付", "nengliang": 100, "jilei": 2},
#      {"xingwei": "网络购物", "nengliang": 80, "jilei": 3},
#      {"xingwei": "共享单车", "nengliang": 200, "jilei": 0}, ]
#
# print("欢迎你来到支付宝的蚂蚁森林，可以进行一下环保行为来积累能量：")
# print("日常的走步---20g\n 生活缴费---50g\n线下支付--100g\n网络购票--80g\n共享单车:200g")
# while True:
#     print("请选择你要进行的操作：1--积累能量，2--查询，0--退出程序")
#     x = int(input())
#     if x == 1:
#         print("请输入你的环保行为：")
#         x1 = input()
#         for e1 in e:
#             if x1 == e1.get("xingwei"):
#                 e1["jilei"] = e1["jilei"] + e1["nengliang"]
#
#     elif x == 2:
#         sum_e = 0
#         for e1 in e:
#             sum_e = sum_e + e1.get("jilei")
#         if sum_e >= 500:
#             print("总能量为：%d , 恭喜您可以种树了" % sum_e)
#         else:
#             print("总能量为：%d，请继续您的环保行为" % sum_e)
#
#         print("请输入你要查询的环保行为")
#         s = input()
#         for e1 in e:
#             if s == e1.get("xingwei"):
#                 print(e1.get("jilei"))
#
#     elif x == 0:
#         break
#     else:
#         print("输入有误，请重新输入")


'''
7、购物车 功能要求： 要求用户输入总资产，例如： 2000 显示商品列表，让用户根据序号选择商品，加入购物车 购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。 
 goods=[  {"name":"电脑","price":1999}, 
         {"name":"鼠标","price":10}, 
         {"name":"游艇","price":20}, 
         {"name":"美女","price":998}
]
分程度来进行代码编写：
1、简单版：用户只能输入一次商品的序号，购买一个或者多个，就进行结账；
2、进阶版：用户可以多次输入自己想买的商品序号，同一个商品可以购买多个，最后再进行结账
3、高阶版：把显示商品和加入购物车，结算，三个功能定义成三个函数，进行调用
'''

money = input("请输入您的总资产：")
print("==========欢迎来到P9班购物中心==========")
print("======本中心有以下商品功能选购，请按照商品序号进行添加到购物车======")
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
print("商品\t名称\t价格")
for g in goods:  # 遍历列表 取出字典2
    print(goods.index(g) + 1, end="\t")
    for k in g.keys():  # 取出字典中的 key value
        print(g.get(k), end="\t")
    print()

# i = input("请选择你需要购买的商品序号：")
# car = []
# dict1 =[]
# for g in goods:
#     if i == goods.index(g) + 1:
#         for k in g.keys():
#             dict1[k] = 1
#             car.append(dict1)
# print(car)

i = input("请选择你需要购买的商品序号：")
all_price = 0
for g in goods:
    if i == goods.index(g) + 1:
        for k in g.keys():
            pass

