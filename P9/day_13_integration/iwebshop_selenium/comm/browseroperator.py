#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: browseroperator.py
@time: 2021/5/26 20:27
'''

from P9.day_13_integration.iwebshop_selenium.comm.logs import Logging

log = Logging().getloger()


class BrowswerOperator:

    def __init__(self, driver):
        self.driver = driver

    # 第二个地方改进
    # 第三个地方加入日志

    # 切换窗口的函数
    def swithwindows(self, type, type_value):  # type：表示元素识别的方法，type_value：表示方法的元素
        log.info("进行窗口切换...")
        self.handle = self.driver.current_window_handle
        self.driver.find_element(type, type_value).click()
        self.handles = self.driver.window_handles
        for h in self.handles:
            if h != self.handle:
                self.driver.switch_to.window(h)

    # 最大化
    def set_windo_max(self):
        log.info("窗口进行最大化...")
        self.driver.maximize_window()

    # 页面刷新
    def refresh_window(self):
        log.info("页面正在刷新")
        self.driver.refresh()

    # 打开页面
    def get_url(self, url):
        log.info("打开页面 %s " % url)
        self.driver.get(url)
