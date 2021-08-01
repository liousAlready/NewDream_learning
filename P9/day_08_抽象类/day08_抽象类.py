#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day08_抽象类.py
@time: 2021/5/9 10:23
'''

# 抽象类：把类再次进行抽象
# 抽象类中的要包含抽象方法：只要定义没有方法体的方法，由子类就来实现具体实现这个方法

import abc


class People(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def set_name(self):
        pass


class Student(People):
    def set_name(self, name):
        print("Student,set_name = %s" % name)


s = Student()
s.set_name("张三")

# car 类 -- 具体显示车的载人量，载货量，租金
# 载人量，载货量，租金 是由各子类具体实现的
import abc


class Car(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calc(self):
        pass

    def show(self):
        print(self.calc())


class Picar(Car):
    def calc(self):
        return "人数" + "租金" + "货物量"


class Bus(Car):
    def calc(self):
        return "人数" + "租金"


c1 = Bus()
c1.show()

c2 = Picar()
c2.show()