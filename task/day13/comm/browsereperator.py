#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: browsereperator.py
@time: 2021/5/28 20:45
'''

from task.day13.comm.logger import log

from selenium.webdriver.common.by import By

class Browsereperator:
    # login_click = (By.LINK_TEXT, "登录")
    # input_name = (By.NAME, "login_info")
    # input_password = (By.NAME, "password")
    # button_click = (By.CLASS_NAME, "input_submit")

    def __init__(self, driver):
        self.driver = driver

    # # 登录函数
    # def logins(self, username, password):
    #     log.info("正在登陆...")
    #     self.loginhandle = self.driver.window_handles
    #     self.driver.find_element(*self.login_click).click()
    #     self.driver.find_element(*self.input_name).send_keys(username)
    #     self.driver.find_element(*self.input_password).send_keys(password)

    # 搜索商品
    def search(self, type, type_vaule, find):
        log.info("正在搜索商品...")
        self.driver.find_element(type, type_vaule).send_keys(find)
        self.driver.find_element_by_class_name("search_submit").click()

    # 选择商品
    def select_sp(self, type, type_value):
        log.info("选择商品中...")
        # 在商品列表中选择单个商品
        self.driver.find_element(type, type_value).click()

    # 加入购物车
    def add_cart(self, type, tyep_value):
        log.info("加入购物车中...")
        self.driver.find_element(type, tyep_value).click()

    # 下拉悬浮框
    def teardownwindow(self):
        log.info("下拉窗口的悬浮框至底部...")
        self.driver.execute_script('window.scrollBy(0,5000)')

    # 点击单个元素
    def clickr(self, type, type_vaule):
        log.info("我正在点击呢...")
        self.driver.find_element(type, type_vaule).click()

    # 输入内容
    def inputd(self, type, type_value, sendkey):
        log.info("我正在输入内容 %s" % sendkey)
        self.driver.find_element(type, type_value).send_keys(sendkey)

    # 切换iframe窗口
    def tabiframe(self, type, type_value):
        log.info("切换至iframe窗口...")
        self.iframename = self.driver.find_element(type, type_value)
        self.driver.switch_to.frame(self.iframename)

    # 跳出框架
    def tabiframeto(self):
        log.info("跳出iframe框架...")
        self.driver.switch_to.default_content()

    # 选择列表中的地址
    def addresslist(self, type, type_valye):
        log.info("正在挑选地址...")
        add_list = self.driver.find_elements(type, type_valye)
        add_list[0].click()

    # 加入切换窗口的函数  type 方法  type_value 方法的元素
    def swtihwindows(self):
        log.info("我现在切换了一个窗口...")
        self.handle = self.driver.current_window_handle
        self.handles = self.driver.window_handles
        for window in self.handles:
            if window != self.handle:
                self.driver.switch_to.window(window)
    # 窗口最大化
    def windosmax(self):
        log.info("我把页面放到最大啦...")
        self.driver.maximize_window()

    # 刷新页面
    def refushwindos(self):
        log.info("我刷新了整个页面...")
        self.driver.refresh()

    # 打开网址
    def get_url(self, url):
        log.info("我正在打开 %s ..." % url)
        print("打开网址 %s ：" % url)
        self.driver.get(url)
