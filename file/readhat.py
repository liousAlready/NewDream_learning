#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: readhat.py
@time: 2021/5/31 11:03
'''


class ReadHat:
    def __init__(self, onlie_p, histor_p, pinglun, view, tuijianr, chushiredu, chushibili):
        self.onlie_p = onlie_p
        self.histor_p = histor_p
        self.pinglun = pinglun
        self.view = view
        self.tuijianr = tuijianr
        self.chushiredu = chushiredu
        self.chushibili = chushibili

    def readhat(self):
        print("开始计算")
        print("当前在线人数:%s ,累积在线人数: %s,评论数: %s,观看次数: %s,推荐热度：%s,初始热度：%s 初始比例：%s"
              % (self.onlie_p, self.histor_p, self.pinglun, self.view, self.tuijianr, self.chushiredu, self.chushibili))
        readhattt = ((self.onlie_p * 0.4) + (self.histor_p * 0.15) + (self.pinglun * 0.15)
                     + (self.view * 0.1) + (self.tuijianr * 0.2) + self.chushiredu) * self.chushibili
        print(readhattt)

c = ReadHat(2, 5, 10, 2, 1, 250000, 1)
c.readhat()
