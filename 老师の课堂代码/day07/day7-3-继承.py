'''
@File : day7-3.py
@Time : 2021/4/28 21:22
@Author: luoman
'''
# import lib
#
'''
继承: 要发生继承，肯定会出现两个类，父类和子类
     原因：既要保留原来代码具有的功能，又可以使用某些功能具有扩展性
     子类可以继承父类的公有属性和方法，但是不继承私有属性和方法
     python是多继承，一个子类也可以有多个父类,如果父类都有相同的方法或者属性，默认调用第一父类
'''

class Card1:

    def __init__(self, name, pwd, money):
        self.name = name
        self.pwd = pwd
        self.money = money

    def __showmoney(self):
        print('看看钱')

    def cunqian(self, m):
        self.money = self.money+m

    def quqian(self, m):
        if self.money -m >= 0:
            self.money = self.money - m

class Card2:

    def __init__(self, name, pwd, money):
        self.name = name
        self.pwd = pwd
        self.money = money

    def __showmoney(self):
        print('看看钱')

    def cunqian(self, m):
        self.money = self.money+2*m

    def quqian(self, m):
        if self.money -m >= 0:
            self.money = self.money - m

class Credit(Card2, Card1):
    def __init__(self,name, pwd, money, e):
        self.e = e
        # 调用父类的方法有两个：方法一：使用super()
        #super().__init__(name, pwd, money)
        # 方法二：
        Card1.__init__(self, name, pwd, money)

    def quqian(self, m):
        if self.money+self.e -m >= 0:
            self.e = self.e -m
            self.money = self.money - m




# 出现了 信用卡--取钱--可以有额度

c1 = Card1('小张', '123456', 2000)
c1.quqian(2500)
print(c1.money)

c11  = Credit('小小张', '123456', 0, 3000)
c11.cunqian(200)
print(c11.money)
c11.quqian(2500)
print(c11.money)
# c11.__showmoney()

