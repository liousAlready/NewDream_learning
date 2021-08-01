#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: login_page_locs.py
@time: 2021/6/1 10:14
'''


from selenium.webdriver.common.by import By

class Login_page_locs:
    # 登录按钮
    login_click = (By.XPATH, "/html/body/header/div[1]/div/div[2]/div/a[1]")
    # 用户名输入框
    input_name = (By.NAME, "login_info")
    # 密码输入框
    input_password = (By.NAME, "password")
    # 登录按钮
    login_button = (By.CLASS_NAME, "input_submit")
    # 断言是否登录
    login_assert = (By.CSS_SELECTOR,"div.body_toolbar_btn.userinfo a ")
