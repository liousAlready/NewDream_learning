#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day08_ketanglianxi.py
@time: 2021/5/9 10:49
'''

import abc


class Showpay(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def qudao(self):
        pass

    def fukuan(self):
        print("收钱宝到账：",self.qudao(200))


class Weixin(Showpay):
    def qudao(self, money):
        return "%s" % "微信支付" + "%d" % (money+2)


class Zhifubao(Showpay):
    def qudao(self, money):
        return "%s" % "支付宝支付" + "%d" % money

w=Weixin()
w.fukuan()

z =Zhifubao()
z.fukuan()