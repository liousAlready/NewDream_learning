#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day09_selenium.py
@time: 2021/5/12 20:20
'''

# 映入第三库
from selenium import webdriver
from time import sleep


def creatdriver():
    # =============
    # 打开浏览器  - 指令1 - 开启与浏览器之前的对话
    driver = webdriver.Chrome()
    # 窗口最大化
    driver.maximize_window()
    # 设置窗口的大小
    driver.set_window_position(200, 200)
    # 访问百度首页 - 指令2
    driver.get("http://www.xmxbbs.com")
    # 刷新页面
    driver.refresh()
    # 后退一步
    driver.back()
    # 前进一步
    driver.forward()

    # =============
    # 获取浏览器内容：
    # 获取页面的标题
    title = driver.title
    print("当前页面的标题是：", title)
    # 获取页面的url
    url = driver.current_url
    print("当前页面的url是：", url)

    # 获取页面的源代码
    # page_soure = driver.page_source
    # print("当前页面的源代码：", page_soure)

    if '百度' not in title:
        driver.get_screenshot_as_file("../file/xmx.png")
        raise Exception("打开页面失败")

    # =============

    # 关闭浏览器
    # driver.close()
    # 退出浏览器驱动
    driver.quit()  # 尽量采用quit去关闭驱动 减少占用内存


try:
    creatdriver()
except Exception as exc:
    print(exc)
