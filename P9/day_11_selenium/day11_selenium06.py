#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day11_selenium06.py
@time: 2021/5/19 20:13
'''
from selenium import webdriver
import time

# 映入第三库
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By


def demo1():
    # =============
    # 打开浏览器  - 指令1 - 开启与浏览器之前的对话
    driver = webdriver.Chrome()
    # 窗口最大化
    driver.maximize_window()
    # driver.get("http://www.xmxbbs.com")
    driver.get("http://www.baidu.com")


# 从三个页面中选择  hao123页面进行操作
# 需要借助页面的属性：url 或者 标题 或者 源代码
def demo11():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.implicitly_wait(30)
    # 1.打开三个页面
    driver.find_element_by_link_text("新闻").click()
    driver.find_element_by_link_text("hao123").click()
    # 2.获取三个页面的窗口句柄
    handles = driver.window_handles
    # 3.通过 标题或者url 或者源代码 来判断页面是否是自己想要的
    for h in handles:
        driver.switch_to.window(h)
        if 'hao123' in driver.current_url:
            break

    time.sleep(2)
    driver.find_elements_by_link_text("虎扑社区").clear()


demo11()

# 层级定位： 无法定位到需要选取的元素，但是其父元素比较容易定位，通过定位父元素再遍历子元素

def demo12():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.implicitly_wait(30)
    driver.find_element_by_id('form').find_element_by_class_name("bg").find_element_by_id("kw").send_keys("hahah")
    sleep(2)
    driver.quit()


# demo12()


# frame 框架的切换
# html文件的嵌套：使用了iframe嵌套页面
def demo13():
    driver = webdriver.Chrome()
    driver.get("https://www.126.com/")
    driver.implicitly_wait(30)
    # 识别iframe()
    # 方法有两种：1、通过id或者是name直接识别 把name或者id 直接写在driver.switch_to.frame("")中
    # driver.switch_to.frame("x-URS-iframe1621427352107.2886)
    # 2、通过xpath方法定位，然后把定位结果放在frame() 中
    e = driver.find_element_by_xpath('//iframe[starts-with(@id,"x-URS-iframe")]')
    driver.switch_to.frame(e)
    driver.find_element_by_name("email").send_keys("lishouwu")
    driver.find_element_by_name("password").send_keys("hahahaha")
    sleep(2)
    # 从框架中跳回原来的页面
    driver.switch_to.default_content()
    driver.find_element_by_link_text("企业邮箱").click()
    sleep(2)
    driver.quit()


# demo13()


# 弹出框的处理
# alter/confirm/prompt处理
# 确定--accepe()  取消--dismiss() 输入框 send_keys()
# 获取弹出框上的文本 text
def demo14():
    driver = webdriver.Chrome()
    driver.get("file:///Users/lishouwu/Downloads/element_samples.html")
    driver.implicitly_wait(30)
    # 弹出对话框
    driver.find_element_by_name("alterbutton").click()
    sleep(2)
    # 获取对话框上的文本
    text = driver.switch_to.alert.text
    print(text)
    # 点击对话框上的确定
    driver.switch_to.alert.accept()
    sleep(2)

    # 弹出对话框
    driver.find_element_by_name("promptbutton").click()
    sleep(1)
    # 输入内容
    driver.switch_to.alert.send_keys("jaaaava")  # chrome浏览器在弹出框中不会显示输入内容
    sleep(1)
    # 点击确定
    driver.switch_to.alert.accept()
    sleep(1)
    # 点击确定
    driver.switch_to.alert.accept()
    sleep(2)

    driver.find_element_by_name("confirmbutton").click()
    sleep(1)
    # 点击取消
    driver.switch_to.alert.dismiss()
    # 再次点击确定
    driver.switch_to.alert.accept()
    sleep(2)
    driver.quit()


# demo14()

# 下拉框处理
# 很多处理的方法：
'''
1.绝对路径
2.层级定位
3.通过元素属性定位
4.把下拉菜单定义成一个下拉菜单对象
'''

from selenium.webdriver.support.ui import Select


def demo15():
    driver = webdriver.Chrome()
    driver.get("file:///Users/lishouwu/Downloads/element_samples.html")
    driver.implicitly_wait(30)
    # 先通过元素定位的方法 找到select标签
    s_list = driver.find_element_by_id("Selector")
    # 把这个元素定义成一个select对象
    s1 = Select(s_list)
    # 可以通过 Select 对象的三种方法来进行识别option中的值
    # 通过option当中的value值
    s1.select_by_value("banana")
    sleep(2)
    # 通过option的索引
    s1.select_by_index(0)  # option选项的索引是从0开始的
    sleep(2)
    # 通过页面显示的文本
    s1.select_by_visible_text("芒果")
    sleep(2)
    driver.quit()


# demo15()

# js的使用
'''
1、可以使用js控制滚动条
2、可以直接执行js代码
3、可以修改控件的属性
'''


def demo16():
    driver = webdriver.Chrome()
    driver.get("https://www.12306.cn/index/")
    # driver.implicitly_wait(30)
    # 1.控制滚动条
    # driver.execute_script("var q=document.body.scrollTop=10000")
    # driver.execute_script("var q=document.documentElement.scrollTop=10000")
    # driver.execute_script('window.scrollBy(0,5000)')

    # 2.可以直接执行js代码
    # driver.execute_script('alert("hello!")')
    # wl = driver.find_element_by_id("train_date")
    # driver.execute_script("arguments[0].style.border='5pxsolidred'", wl)  # 加边框

    # # 3.可以修改控件的属性
    # # 把出发日期的readonly属性进行删除，然后输入日期
    # js = 'document.getElementById("train_date").removeAttribute("readonly")'
    # driver.execute_script(js)
    # driver.find_element_by_id("train_date").send_keys("P9")

    js = 'document.getElementById("train_date").value="p9"'
    driver.execute_script(js)

    sleep(5)
    driver.quit()


#demo16()
