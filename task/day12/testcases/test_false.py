#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: test_false.py
@time: 2021/5/24 09:19
'''

from task.day12.comm.createrbrower import Creater
import time

class TestLogin(Creater):
    '''测试购物商场登录用例'''

    # 测试登录
    def test_loginf(self):
        """错误的用户名"""
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_name("login_info").send_keys("wwww")
        self.driver.find_element_by_name("password").send_keys("111111")
        self.driver.find_element_by_class_name("input_submit").click()
        self.assertIn("账号或密码错误", self.driver.find_element_by_xpath('/html/body/div[3]/section/section/form/div').text)

    def test_loginf1(self):
        """错误的密码"""
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_name("login_info").send_keys("nswe")
        self.driver.find_element_by_name("password").send_keys("1223123123")
        self.driver.find_element_by_class_name("input_submit").click()
        self.assertIn("账号或密码错误", self.driver.find_element_by_xpath('/html/body/div[3]/section/section/form/div').text)

    # def test_loginf2(self):
    #     """不输入账号"""
    #     self.driver.find_element_by_link_text("登录").click()
    #     self.driver.find_element_by_name("login_info").send_keys()
    #     self.driver.find_element_by_name("password").send_keys("1223123123")
    #     self.driver.find_element_by_class_name("input_submit").click()
    #     self.assertIn("nswe，用户登录成功", self.driver.find_element_by_css_selector("div.body_toolbar_btn.userinfo a ").text)
    #
    # def test_loginf3(self):
    #     """不输入密码"""
    #     self.driver.find_element_by_link_text("登录").click()
    #     self.driver.find_element_by_name("login_info").send_keys("nswe")
    #     self.driver.find_element_by_name("password").send_keys()
    #     self.driver.find_element_by_class_name("input_submit").click()
    #     self.assertIn("nswe，用户登录成功", self.driver.find_element_by_css_selector("div.body_toolbar_btn.userinfo a ").text)
