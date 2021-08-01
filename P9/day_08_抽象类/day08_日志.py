#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day08_日志.py
@time: 2021/5/9 16:37
'''
import logging
import time


class Logging:
    def __init__(self, logger=None):
        '''
        指定日志的级别，日志的存放路径，日志输出的格式
        :param logger:
        '''

        # 创建日志对象
        self.logger = logging.getLogger(logger)
        # 设置日志的最低级别
        self.logger.setLevel(logging.DEBUG)
        # 设置日志文件的文件及路径
        self.logpath = '/Users/lishouwu/PycharmProjects/NewDream_learning/P9/file/logs'
        self.logtime = time.strftime("%Y_%m_%d_%H_%M_%S")
        self.logname = self.logpath + self.logtime + ".log"
        # 创建日志文件对象
        fp = logging.FileHandler(self.logname, "a", encoding="utf-8")
        fp.setLevel(logging.INFO)

        # 定义日志内容的输出格式

        formatter = logging.Formatter("%(asctime)s"
                                      '-%(name)s'
                                      "-%(levelname)s"
                                      "-%(message)s")
        # 把日志格式对象驾到日志文件对象
        fp.setFormatter(formatter)
        self.logger.addHandler(fp)

    def getloger(self):
        return self.logger
