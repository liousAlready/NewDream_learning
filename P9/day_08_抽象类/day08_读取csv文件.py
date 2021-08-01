#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day08_读取csv文件.py
@time: 2021/5/9 14:49
'''

import csv
from P9.day_08_抽象类.day08_日志 import Logging

log = Logging().getloger()

class ReadCsv:

    def readcsv(self,filename):
        fp = open(filename, "r+", encoding="utf-8")
        content = csv.DictReader(fp)
        print(content)
        self.list = []

        for c in content:

            if content.line_num == 1:
                continue
            else:
                list.append(c)

        return list

    def getindex(self, filename, n):
        return self.readcsv(filename)[n]["序号"]

    def getname(self, filename, n):
        return self.readcsv(filename)[n]["名字"]

    def getpeopleconut(self, filename, n):
        return self.readcsv(filename)[n]["人数"]

    def getloads(self, filename, n):
        return self.readcsv(filename)[n]["载重"]

    def getgoods(self, filename, n):
        return self.readcsv(filename)[n]["租金"]


filename = "../../file/car1.csv"
r1 = ReadCsv()
r1.getname(2)
