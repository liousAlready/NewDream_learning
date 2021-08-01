#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day08_多态.py
@time: 2021/5/9 11:19
'''

# 多态进行使用：继承 方法的重写：具有不同功能的函数可以使用相同的函数名


import abc


class File(metaclass=abc.ABCMeta):  # 同一类事物:文件
    @abc.abstractmethod
    def click(self):
        pass


class Text(File):
    # 文件的形态之一:文本文件
    def click(self):
        print('open file')


class ExeFile(File):
    # 文件的形态之二:可执行文件
    def click(self):
        print('execute file')


def openFile(obj):
    obj.click()


txt = Text()
exe = ExeFile()
openFile(exe)
