#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: login_datas.py
@time: 2021/6/1 15:03
'''

# 登录成功的数据
user = ("nswe", "111111")

# 登录失败的数据- 用户名为空/密码为空/用户名格式不正确
invalid_data = [
    {"user": "", "password": "111111", "check": "账号或密码错误"},
    {"user": "nswe", "password": "1111112qsda1", "check": "账号或密码错误"},
    {"user": "adsasdas", "password": "111111", "check": "账号或密码错误"}
]
