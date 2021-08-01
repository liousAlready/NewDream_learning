#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day08_日志.py
@time: 2021/5/9 16:37
'''
import logging
import time
from P9.day_13_integration.iwebshop_selenium.comm.config import Config

conf = Config()


class Logging:
    def __init__(self, logger=None):
        # 创建日志对象
        self.logger = logging.getLogger(logger)
        # 设置日志的最低级别
        self.logger.setLevel(logging.DEBUG)
        # 设置日志文件的名字及路径
        self.logpath = conf.logpath
        self.logtime = time.strftime('%Y_%m_%d_%H_%M_%S')
        self.logname = self.logpath + self.logtime + '.log'
        # 创建日志文件对象
        fp = logging.FileHandler(self.logname, 'a', encoding='utf-8')
        fp.setLevel(logging.INFO)

        # 设置日志内容的输出格式

        formatter = logging.Formatter('%(asctime)s '
                                      '-%(filename)s'
                                      '-%(levelname)s '
                                      '- %(message)s')
        # 把日志格式对象加到日志文件对象
        fp.setFormatter(formatter)
        self.logger.addHandler(fp)

    def getloger(self):
        return self.logger
