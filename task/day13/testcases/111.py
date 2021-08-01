#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: 111.py
@time: 2021/6/1 16:00
'''

import ddt
import unittest


@ddt.data
class Test(unittest.TestCase):
    name = {'name': '王荔', 'age': 11}

    @ddt.data(name)
    def test(self, name):
        print(name)


if __name__ == '__main__':
    unittest.main()
