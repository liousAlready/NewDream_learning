#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day10_selenium3.py
@time: 2021/5/16 11:03
'''

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
    # 2.通过name方法
    # driver.find_element_by_name("srchtxt").send_keys("python")
    # 3.通过class属性方法：class_name
    # driver.find_element_by_class_name("pn").click()
    # driver.find_element_by_tag_name("area").click()

    # 5.通过链接文本来进行识别   一定是要a标签上的文本
    driver.find_element_by_link_text("新闻").click()
    driver.find_element_by_partial_link_text("新").click()  # 通过文本的一部分内容进行识别

    # 6.通过xpath进行识别


# Xpath
# 有六种小方法来找元素

def damo2():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    # 1.绝对路径的方法 必须从html标签开始，以/开头
    # driver.find_element_by_xpath("/html/body/div/div/div[3]/a").click() # 如果同一级别标签名相同，则需要使用下标定位
    # 2.相对路径 以//开头
    # driver.find_element_by_xpath("//div/div[3]/a").click()
    # 3.元素索引定位 结合相对路径或绝对路径
    # 4.通过元素的属性值进行定位  "//标签名[@属性="属性值"]"
    # 支持and 和 or 关键字，多个属性一起定位元素
    # driver.find_element_by_xpath('//input[@maxlength="255"] and @id="kw').send_keys("selenium")
    # 5.进行模糊匹配--元素的属性值可能是动态变化的
    # 元素属性值开头包含内容 ：starts-with()
    # driver.find_element_by_xpath('//a[starts-with(@name,"tj_briicon")]').click()
    # 元素属性值结尾包含内容：substring()
    # driver.find_element_by_xpath('//a[substring(@name,7)="icon]').click()
    # 元素属性值结尾包含内容：contains()
    # driver.find_element_by_xpath('//a[contains(@name,"J_bri"]').click()
    # 6.使用元素文本进行定位 通过text()进行获取  不一定只有a标签才有文本
    #  driver.find_element_by_xpath('//span[text()="国家卫健委派出工作组赴辽宁"]').click()
    driver.find_element_by_xpath('//span[contains(text(),"国家卫健委")]').click()

    sleep(2)


# damo2()

# 第七种元素识别的方法 Css_selector
def damo3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://www.baidu.com")
    # 1.使用绝对路径  从html开始 使用id或者class属性进行标记
    # driver.find_element_by_css_selector("html body div#wrapper div#head div#s-top-left a.c-font-normal ").click()
    # 2.使用相对路径
    # driver.find_element_by_css_selector("div#head div#s-top-left a.c-font-normal ").click()
    # 3.使用元素属性  标签名[属性="属性名"]
    driver.find_element_by_css_selector('a[name="tj_briicon"][class="s-bri"]').click()
    # 4.使用模糊定位：属性值如果太长或网页中的元素属性动态变化
    # $：以..结束 ^:以什么开头 *：包含
    # driver.find_element_by_css_selector('a[name^="tj_bri"]').click()
    # driver.find_element_by_css_selector('a[name$="iicon"]').click()
    # driver.find_element_by_css_selector('a[name*="brii"]').click()
    # 5. 子元素
    # driver.find_element_by_css_selector("form span input").send_keys("selenium")
    # driver.find_element_by_css_selector("form>span>input").send_keys("selenium")
    # driver.find_element_by_css_selector('div#s-top-left a:first-child').click()
    # driver.find_element_by_css_selector('div#s-top-left a:last-child').click()
    # driver.find_element_by_css_selector('div#s-top-left a:nth-child(3)').click()
    # 6.查询兄弟元素
    #driver.find_element_by_css_selector('div#s-top-left a +a+a').click()
    #driver.find_element(By.CSS_SELECTOR,"div#s-top-left a +a+a").click()

    sleep(2)


damo3()
