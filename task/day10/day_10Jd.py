#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day_10Jd.py
@time: 2021/5/17 09:57
'''

# 映入第三库
from selenium import webdriver
from time import sleep
import random


def Jd_addcart():
    # 打开浏览器  - 指令1 - 开启与浏览器之前的对话
    driver = webdriver.Chrome()
    driver.get("http://www.jd.com")
    # 获取当前页面的句柄
    now_bing = driver.current_window_handle
    print(now_bing)
    # 添加隐式等待
    driver.implicitly_wait(5)
    # 定位输入框元素
    input_box = driver.find_element_by_css_selector('input[id="key"][class="text"]')
    input_box.send_keys("冰淇淋")
    # 定位搜索元素
    sreech = driver.find_element_by_css_selector('button[class="button"][aria-label="搜索"]')
    sreech.click()
    # 取这个元素下的兄弟函数列表
    list = driver.find_elements_by_css_selector("li.gl-item div.gl-i-wrap div.p-img a img")
    # list1 = driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img')
    print("所有的商品图片：", len(list))
    bro = random.randrange(0, len(list) - 1)

    # 点击商品列表，跳转到详情
    list[bro].click()
    # 点击单个商品商品，跳转到详情
    # list1.click()

    # 获取新页面句柄
    new_bing = driver.window_handles  # 句柄列表
    print(new_bing)
    for n in new_bing:  # 遍历句柄列表
        if n != new_bing:
            driver.switch_to.window(n)
    # 查看元素是否存在
    add_cart = driver.find_element_by_id('InitCartUrl')
    print("购物车按钮是否可见：", add_cart.is_displayed())
    # 点击加入购物车
    add_cart.click()
    # 当前页面截图
    driver.get_screenshot_as_file("../购物车页面.png")
    sleep(1)
    # 切换到之前的搜索页面
    driver.switch_to.window(now_bing)
    # 给你看一下效果
    sleep(2)
    # 释放缓存
    driver.quit()


Jd_addcart()
