#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: config.py
@time: 2021/5/26 21:24
'''

import configparser


class Configs:
    def __init__(self):
        self.configpath = '/Users/lishouwu/Documents/PycharmProjects/NewDream_learning/P9/weixin_apitest/conf/conf.ini'  # .ini文件的路径
        self.conf = configparser.ConfigParser()  # 定义读取.ini文件的对象
        self.conf.read(self.configpath, encoding='utf-8')

        self.url = self.conf.get('browser', 'gettonken')
        self.casedir = self.conf.get('filepath', 'casedir')
        self.logpath = self.conf.get('filepath', 'logpath')
        self.reportpath = self.conf.get('filepath', 'reportpath')