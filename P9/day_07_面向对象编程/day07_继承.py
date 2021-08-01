#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day07_继承.py
@time: 2021/5/7 21:44
'''

'''
继承：要发生继承，肯定会出现两个类，父类跟子类
     原因：既要保留原来代码具有的功能，又可以使某些功能具有扩展性
    子类可以继承父类的公有属性和方法，但是不能继承私有属性和方法
    
    python当中是多继承，一个子类可以有多个父类
    如果父类都有相同的方法或者属性，默认调用第一父类的
'''


class Card:

    def __init__(self, name, password, money):
        self.name = name
        self.password = password
        self.money = money

    def __showmoney(self):
        print("看看钱")

    def cunqian(self, m):
        self.money = self.money + m

    def quqian(self, m):
        if self.money - m >= 0:
            self.money = self.money - m
            print("您这次取了 %s " % self.money)
        else:
            print("余额不足")


class Card1:

    def __init__(self, name, password, money):
        self.name = name
        self.password = password
        self.money = money

    def __showmoney(self):
        print("看看钱")

    def cunqian(self, m):
        self.money = self.money + 2*m

    def quqian(self, m):
        if self.money - m >= 0:
            self.money = self.money - m
            print("您这次取了 %s " % self.money)
        else:
            print("余额不足")


class SubCard(Card1, Card):  # 括号里面有多个父类，可以继承多个父类
    def __init__(self, name, password, money, edu):
        self.edu = edu
        # 调用父类的方法有两个

        # 方法一:使用super()
        # super().__init__(name, password, money)

        # 方法二：写上父类名.方法
        Card.__init__(self, name, password, money)

    def quqian(self, m):
        if self.money + self.edu - m >= 0:
            self.edu = self.edu - m
            self.money = self.money - m
            print("您这次取了 %s " % self.money)
        else:
            print("余额不足")


c1 = Card("小王", 123456, 1000)
c1.quqian(2500)


c11 = SubCard("小王八", 12221, 0, 3000)
c11.cunqian(200)
print(c11.money)
c11.quqian(2500)
