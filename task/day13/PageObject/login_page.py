#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: login_page.py
@time: 2021/5/31 22:17
'''

from task.day13.comm.logger import log
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from task.day13.PageLocators.login_page_locs import Login_page_locs as locs
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.remote.webdriver import WebDriver


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # 登录函数
    def login(self, username, password):
        log.info("正在登陆...")
        self.wait.until(EC.visibility_of_element_located(locs.login_button))
        time.sleep(2)
        self.driver.find_element(*locs.login_click).click()
        self.driver.find_element(*locs.input_name).send_keys(username)
        self.driver.find_element(*locs.input_password).send_keys(password)
        self.driver.find_element(*locs.login_button).click()

    # # 登录失败
    # def get_error_msg_from_login_area(self):
    #     """
    #     获取登录失败时，在登录区域的提示。
    #     :return:
    #     """
    #     log.error("登录失败...")
    #     self.wait.until(EC.visibility_of_element_located(locs.login_assert))
    #     return self.driver.find_element(*locs.login_assert).text
