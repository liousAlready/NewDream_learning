#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: test_false.py
@time: 2021/5/24 09:19
'''

from task.day13.comm.createrbrower import CreaterBrower
from selenium.webdriver.common.by import By


class Testfalse(CreaterBrower):
    '''测试购物商场逆向用例'''

    def test_loginf(self):
        """错误的用户名"""
        self.bo.logins("nswe122", "111111", By.LINK_TEXT, "登录")
        self.assertIn("账号或密码错误", self.driver.find_element_by_xpath('/html/body/div[3]/section/section/form/div').text)

    def test_loginf1(self):
        """错误的密码"""
        self.bo.logins("nswe122", "111111", By.LINK_TEXT, "登录")
        self.assertIn("账号或密码错误", self.driver.find_element_by_xpath('/html/body/div[3]/section/section/form/div').text)
