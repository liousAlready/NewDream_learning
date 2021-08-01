#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day06.py
@time: 2021/4/22 10:39
'''

'''
1、定义名为Number的类
其中有两个整型数据成员n1和n2
编写构造方法：赋予n1和n2初始值
再为该类定义加（addition）、减（subtration）、乘（multiplication）、除（division）等公有对象方法
分别对两个成员变量执行加、减、乘、除的运算。 
创建Number类的对象，调用各个方法，并显示计算结果。
'''

# class Number:
#     print("===调用Number类===")
#
#     def __init__(self, n1, n2):
#         self.n1 = n1
#         self.n2 = n2
#
#     def addition(self):
#         return self.n1 + self.n2
#
#     def subtration(self):
#         return self.n1 - self.n2
#
#     def multiplication(self):
#         return self.n1 * self.n2
#
#     def division(self):
#         return self.n2 / self.n2
#
#
# ne = Number(8, 4)
# print(ne.addition())
# print(ne.subtration())
# print(ne.multiplication())
# print(ne.division())

"""
请定义一个名为Card的扑克牌类，该类有两个字符串变量face和suit。
分别描述一张牌的牌面值（如：A,K,Q,J,10,9…3,2）和花色（如：黑桃，红桃，梅花，方块）。
定义Card类中的构造方法，为类中的成员变量进行初始化； getFace()，得到扑克牌的牌面值；
定义方法getSuit（）,得到扑克牌的花色；定义__str__()，返回表示扑克牌的花色和牌面值字符串（如：红桃A，梅花10）；
在测试模块中定义字符串数组f和s：分别表示扑克牌的牌面值和花色；
定义52个元素的deck列表，用来存放52张牌。
"""
suit = ["黑桃", "红桃", "梅花", "方块"]

class Card:
    ''' 创建一个Card 类'''


    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

    # 获取牌面
    def getFace(face):
        return face

    # 获取花色
    def getSuit(suit):
        return suit

    # 获取花色+牌面
    def __str__(self):
        """返回一个对象的描述信息"""
        # print(num)
        return "牌面是:%s , 花色是:%d" % (self.face, self.suit)


# face = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
# suit = ["黑桃", "红桃", "梅花", "方块"]
# for n in face:  # 循环 数字
#     for i in suit:  # 循环 花色
#         print(i, n)

face = ["A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2", "1"]
suit = ["黑桃", "红桃", "梅花", "方块"]

# 获取牌面
des = Card.getFace(face)
print(des)

# 获取花色
facea = Card.getSuit(suit)
print(facea)
