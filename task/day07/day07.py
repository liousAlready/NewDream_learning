#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day07.py
@time: 2021/5/7 22:39
'''

'''
为公司解决智能租车问题，根据客户选定的车型和租车天数，来计算租车费用，最大载客人数，最大载载重量。
公司现有三种车型（客车、皮卡车、货车），每种车都有名称和租金的属性；其中：客车只能载人，货车只能载货，皮卡车是客货两用车，即可以载人，也可以载货。
下面是答答租车公司的可用车型、容量及价目表：
序号     名称     载客量      载货量        租金
                           （人）     （吨）    （元/天）
  1          A            5                                 800
  2          B            5                                 400
  3          C            5                                 800
  4          D            51                             1300
  5          E            55                             1500
  6          F             5            0.45             500
  7         G             5             2.0               450
  8         H                            3                  200
  9          I                             25              1500
 10        J                             35              2000

要求：根据客户输入的所租车型的序号及天数，计算所能乘载的总人数、货物总数量及租车费用总金额。
Input
首行是一个整数：代表要不要租车 1——要租车（程序继续），0——不租车（程序结束）；
第二行是一个整数，代表要租车的数量N；
接下来是N行数据，每行2个整数m和n，其中：m表示要租车的编号，n表示租用该车型的天数。
Output
若成功租车，则输出一行数据，数据间有一个空格，含义为：
载客总人数 载货总重量（保留2位小数） 租车金额（整数）
若不租车，则输出： 
0 0.00 0（含义同上）
'''


class Car:

    def __init__(self, carname, rents):
        self.carname = carname
        self.rents = rents


class Bus(Car):
    def __init__(self, carname, rents, peplecount):
        self.peplecount = peplecount
        Car.__init__(self, carname, rents)

    def __str__(self):
        return "%5s" % self.carname + "%12d" % self.peplecount + "%24d" % self.rents


class Truck(Car):
    def __init__(self, carname, rents, goods):
        self.goods = goods
        Car.__init__(self, carname, rents)

    def __str__(self):
        return "%5s" % self.carname + "%25.2f" % self.goods + "%10d" % self.rents


class Pica(Car):
    def __init__(self, carname, rents, goods, peplecount):
        self.peplecount = peplecount
        self.goods = goods
        Car.__init__(self, carname, rents)

    def __str__(self):
        return "%5s" % self.carname + "%12d" % self.peplecount + "%13.2f" % self.goods + "%10d" % self.rents
