#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day10_selenium5.py
@time: 2021/5/16 16:11
'''

# 映入第三库
from selenium import webdriver
from time import sleep

# 场景的处理
# 等待处理
# 等待页面加载元素后再进行操作，selenium提供三种等待时间设置方式

# 固定等待 sleep() 设置多长时间，就必须等待多久时间

# 隐式等待：implictilyWait() 比固定等待要灵活，只要在规定的时间内，元素被找到的话，那么就不再等待
#         全局等哒i:从隐式等待设置的位置开始往后进行元素识别时，每一次都会去启动等待

# 显示等待：WebDriberWati() 等待一个条件满足之后那个不再等待了，否则跑出异常
# 不是全局等待，每一个条件都需要设置等待

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def demo8():
    # 打开浏览器  - 指令1 - 开启与浏览器之前的对话
    driver = webdriver.Chrome()

    driver.get("http://www.baidu.com")
    # 隐式等待5s
    # driver.implicitly_wait(5)  # 只要元素被识别到，就不再等
    # 假设知道页面包含"百度一下"
    # WebDriverWait(driver, 10, 0.5).until(EC.title_contains("百度一下"))
    # 假设  异常案例
    WebDriverWait(driver, 10, 0.5).until(EC.title_contains("P9"))  # 抛出异常事件
    driver.find_element_by_id("kw").send_keys("java")
    # driver.find_element_by_id("sakdsad").send_keys("java")
    sleep(2)


# demo8()


# 二、识别一组元素  通过某一个共同的属性及属性值，找到所有的元素
import random


def demo9():
    # 打开浏览器  - 指令1 - 开启与浏览器之前的对话
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")

    # 识别出所有的a标签 存入到一个列表中
    # list1 = driver.find_elements_by_tag_name("a")
    # print(len(list1))
    list2 = driver.find_elements_by_class_name("mnav")  # 返回的是列表
    print(len(list2))
    r = random.randint(0, len(list2) - 1)
    list2[r].click()
    sleep(2)

    driver.quit()


# demo9()


# 三、窗口的切换
'''
多窗口切换：窗口句柄--唯一表示窗口的字符串

1、打开第一个页面后，获取第一个页面的窗口句柄
2、打开新的页面
3、获取两个页面的窗口句柄
4、通过对窗口句柄进行判断，跳转到新的窗口，然后继续进行操作
'''


def demo10():
    # 打开浏览器  - 指令1 - 开启与浏览器之前的对话
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.implicitly_wait(5)
    # 当页面因为某个元素的操作新打开一个标签，但是driber还留在原来的标签页
    # 此时如果需要在新的标签页进行操作的话，必须把driver跳转到新的页面，才能进行操作
    # 1.获取第一个句柄
    now_hadle = driver.current_window_handle
    # 2.打开新页面
    driver.find_element_by_link_text("新闻").click()
    # 3.获取两个页面的窗口句柄
    hadle = driver.window_handles
    # 4.通过窗口句柄进行判断，跳转到新的窗口，然后进行操作
    for h in now_hadle:
        if h != now_hadle:
            driver.switch_to.window(h)
    sleep(2)
    driver.find_element_by_link_text("国际").click()
    # 假设在新的窗口上操作完成，需要返回到原来的串钩
    driver.switch_to.window(hadle)
    driver.quit()


demo10()
