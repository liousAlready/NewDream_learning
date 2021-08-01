#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: config.py
@time: 2021/5/26 21:24
'''

import configparser


# ini 文件是由sections 和option组成的
class Config:
    def __init__(self):
        self.configpath = "/Users/lishouwu/Documents/PycharmProjects/NewDream_learning/P9/day_13_integration/iwebshop_selenium/conf/conf.ini"  # .ini文件的路径
        self.conf = configparser.ConfigParser()  # 定义读取ini文件的对象
        self.conf.read(self.configpath, encoding='utf-8')
        # print(conf.sections())  # 获取所有的sections []

        # 浏览器
        self.url = self.conf.get('browser', 'url')
        self.browsername = self.conf.get('browser', 'browsername')
        #  文件路径
        self.reportpath = self.conf.get('filepath', 'reportpath')
        self.logpath = self.conf.get('filepath', 'logpath')
        self.casedir = self.conf.get('filepath', 'casedir')


class Configs:
    def __init__(self):
        self.configpath = '/Users/luoman/python_code/p9_code/baidu_selenium_demo/conf/conf.ini'  # .ini文件的路径
        self.conf = configparser.ConfigParser()  # 定义读取.ini文件的对象

        self.conf.read(self.configpath, encoding='utf-8')
        # print(conf.sections()) # 获取所有sections

        self.url = self.conf.get('browser', 'url')
        self.browsername = self.conf.get('browser', 'browsername')

        self.casedir = self.conf.get('filepath', 'casedir')
        self.logpath = self.conf.get('filepath', 'logpath')
        self.reportpath = self.conf.get('filepath', 'reportpath')
