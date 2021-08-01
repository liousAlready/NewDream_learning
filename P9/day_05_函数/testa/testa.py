#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: testa.py
@time: 2021/4/18 14:20
'''


def helloprint(n):
    print("hello" * n)


# 以下指示测试的代码，不想其他模块在import的时候被使用，那需要加入
if __name__ == '__main__':
    print("hello testa，测试自身执行时会不会执行")
    helloprint(2)

print("hello testa --测试b模块引用时是否会执行")
helloprint(2)
# __name__ 是一个系统的内置变量，指的是模块的名字
# 当自身运行时，__name__ ==
print(__name__)
# 当其他模块导入自身后，由其他模块运行，我的__name__变成了？