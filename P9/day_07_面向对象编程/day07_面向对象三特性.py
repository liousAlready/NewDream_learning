#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day07_面向对象三特性.py
@time: 2021/4/30 14:48
'''

# 面向对象编程的三大特性：封装、继承、多态
# 同一个项目肯定不是一个人开发的，如何节省时间，如何减少维护的成本
# 实现与使用分离  高内聚 低耦合
'''
封装：
    原因：1.保护代码的安全 : 不希望实例属性在外部被修改或者直接引用，要求把实例属性改成私有实例属性
           如何调用封装元素：需要通过公共的实例方法进行引用
           也可以把方法封装成私有方法，只能在类的内部使用，类的外部是不能直接使用的
         2.降低代码的复杂程度
'''


class Qishou:
    name = "美团骑手"

    @classmethod
    def talk(cls):  # 定义了一个类方法   cls <= class
        print("您好，您的外卖到了")
        cls.name = "美团小帮手"  # 对类属性进行修改

    @classmethod
    def good(cls):  # 定义了一个类方法
        print("记得五星好评哦~")

    @staticmethod
    def songcan():  # 定义了一个静态方法
        print("已经开始配送了！")

    def __init__(self, name, phone):  # 每个对象在初始化的时候 需要不同的值 就需要构造方法
        self.__name = name  #
        self.__phone = phone

    def getname(self, s):  # 获取私有属性的值
        if s == "经理":
            return self.__name
        else:
            return "没有权限"

    def setname(self, name, phone):  # 对私有属性进行赋值
        if self.__phone == phone:
            self.__name = name

    def __shouaddress(self):
        print("%s ,请问你在哪里" % self.__name)

    def __isplay(self):
        print("%s 是否到了" % self.__name)

    def showqishou(self):
        self.__shouaddress()
        self.__isplay()

    def __str__(self):  # 假设实例输出的格式是：我是xxx，我的联系方式是xxx
        return '我是%s。我的联系方式是%s' % (self.__name, self.__phone)




q1 = Qishou("张三", 1557282821)  # 创建对象的时候，就自动调用构造方法，通过类名
q1.setname("张小三", 1557282221)
print(q1.getname("经理"))  # 通过传入参数  再调用实例化属性
q1.showqishou()
