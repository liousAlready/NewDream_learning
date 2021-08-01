#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day10_selenium4.py
@time: 2021/5/16 14:51
'''

# 映入第三库
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


# 常用元素操作的API

def demo4():
    # 打开浏览器  - 指令1 - 开启与浏览器之前的对话
    driver = webdriver.Chrome()
    # 窗口最大化
    driver.maximize_window()
    # driver.get("http://www.xmxbbs.com")
    driver.get("http://www.baidu.com")
    # clear() 清楚元素中的内容  输入框为默认值时，可以进行清空，避免影响
    driver.find_element_by_id("kw").send_keys("ashdjahsd")
    sleep(2)
    driver.find_element_by_id("kw").clear()
    sleep(2)
    driver.quit()

    '''
    submit():提交表单，要求对象必须是表单，父标签必须是form
    driver.find_element(By.ID,'form').submit()
    '''


# demo4()


def demo5():
    # 打开浏览器  - 指令1 - 开启与浏览器之前的对话
    driver = webdriver.Chrome()
    driver.get("http://www.12306.cn/index")
    # 获取元素的尺寸
    e = driver.find_element_by_id("fromStationText")
    size = e.size
    print("尺寸：", size)
    # 获取元素的坐标  坐标原点(0,0)是屏幕的左上角
    location = e.location
    print("坐标：", location)
    e1 = driver.find_element_by_class_name("form-label")
    print("文本：", e1.text)
    # 是否被选中
    e2 = driver.find_element_by_id("isStudentDan")
    print("是否被选中前", e2.is_selected())
    e2.click()
    print("是否可见：", e.is_displayed())
    print("是否可用：", e.is_enabled())
    print("获取标签名：", e.tag_name)
    print("获取属性：", e.get_attribute("type"))
    print("获取出发日期的readonly的值", driver.find_element_by_id("train_date").get_attribute("readonly"))
    sleep(2)


# demo5()


# 鼠标跟键盘操作
# 鼠标：单击 双击 右击鼠标，拖动鼠标，把鼠标放在某个元素上面
from selenium.webdriver.common.action_chains import ActionChains


def demo6():
    # 打开浏览器  - 指令1 - 开启与浏览器之前的对话
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    # 右击鼠标
    # 1.定义鼠标对象
    mouse = ActionChains(driver)
    # 2.识别元素
    e = driver.find_element_by_id("kw")
    # 3.在元素上进行鼠标操作
    mouse.context_click(e).perform()
    sleep(2)
    mouse.release(e).perform()  # 释放鼠标资源
    driver.quit()
    # 把鼠标放在某一个元素上
    e1 = driver.find_element_by_name("tj_briicon")
    mouse.move_to_element(e1).perform()
    sleep(2)


# demo6()

from selenium.webdriver.common.keys import Keys


def dome7():
    # 打开浏览器  - 指令1 - 开启与浏览器之前的对话
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")

    e = driver.find_element_by_id("kw")
    e.send_keys("hahahahahahhhh")
    sleep(2)
    # e.send_keys(Keys.BACKSPACE)
    sleep(2)
    e.send_keys(Keys.TAB)
    # sleep(2)

    # ctrl+a ctrl+c ctrl+v
    # 先创建键盘对象
    k = ActionChains(driver)
    k.key_down(Keys.COMMAND).send_keys("c").key_up(Keys.CONTROL).perform()
    k.key_down(Keys.COMMAND).send_keys("v").key_up(Keys.CONTROL).perform()
    sleep(2)




dome7()
