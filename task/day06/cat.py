#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: cat.py
@time: 2021/4/27 10:07
'''


class PowerOfTwo:
    def __init__(self):
        self.exponent = 0  # 将每次的指数记录下来

    def __next__(self):
        if self.exponent > 10:
            raise StopIteration
        else:
            result = 2 ** self.exponent  # 以 2 为底数求指数幂
            self.exponent += 1
            return result

    def __iter__(self):
        return self


p = PowerOfTwo().__next__()
print(p)
