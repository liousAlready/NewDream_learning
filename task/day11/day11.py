#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day11.py
@time: 2021/5/20 09:05
'''

'''
http://shop.aircheng.com/site/index
从登陆—判断登陆是否成功—输入搜索商品的关键字—搜索——选择商品进行详情页面—加入购物车—提交订单—新增收货地址—支付—支付成功(截图)
'''
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
import random

def Addcart():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("http://shop.aircheng.com/site/index")
    driver.implicitly_wait(5)

    # 登录
    login = driver.find_element_by_link_text("登录")
    login.click()

    # 定位用户名
    user_name = driver.find_element_by_name("login_info")
    # 输入用户
    user_name.send_keys("nswe")
    # 定位密码
    user_password = driver.find_element_by_name("password")
    # 输入密码
    user_password.send_keys("111111")
    # 点击登录
    driver.find_element_by_class_name("input_submit").click()
    # 获取当前登录用户的名称
    c = driver.find_element_by_css_selector("div.body_toolbar_btn.userinfo a ").text
    if c == "nswe":
        print("nswe，用户登录成功")
    else:
        print("当前登录账号不是nswe")

    # 点击输入框，并输入信息
    serchee = driver.find_element_by_name("word")
    serchee.send_keys("真皮女包")
    # 点击搜索框
    driver.find_element_by_class_name("search_submit").click()

    # 断言当前页面是否为跳转页面
    time.sleep(2)
    c = driver.title
    # 判断当前页面标题是否为搜索的内容
    if "真皮女包" in c:
        print("当前页面跳转成功")
    else:
        print("页面跳转失败")

    # 获取当前页面商品的列表
    list1 = driver.find_elements_by_css_selector(".goods_list ul li a")
    time.sleep(2)
    add = random.randrange(0, len(list1) - 1)
    list1[add].click()
    #driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/section/section[2]/ul/li[1]/a/img").click()

    # 切句柄
    hadels = driver.window_handles
    print(hadels)
    for n in hadels:  # 遍历句柄列表
        if n != hadels:
            driver.switch_to.window(n)

    time.sleep(2)
    add_ca = driver.find_element_by_css_selector("#joinCarButton > span")
    # 查看购物车按钮是否存在
    print("购物车按钮是否可见：", add_ca.is_displayed())
    add_ca.click()

    # 鼠标悬浮至购物车元素
    # 定义一个鼠标变量
    mouse = ActionChains(driver)
    go_cart = driver.find_element_by_class_name("go_cart")
    # 将鼠标移到购物车图标
    mouse.move_to_element(go_cart).perform()
    # 点击结算按钮
    driver.find_element_by_link_text("结算").click()
    # 下拉悬浮框
    driver.execute_script('window.scrollBy(0,5000)')
    # 点击去结算按钮
    driver.find_element_by_link_text("去结算").click()

    # 添加地址
    driver.find_element_by_link_text("添加新地址").click()
    # 定位iframe框
    new_yemian = driver.find_element_by_xpath('//iframe[starts-with(@name,"OpenaddressWindow")]')
    driver.switch_to.frame(new_yemian)
    # 定位到姓名
    driver.find_element_by_css_selector('.__address_alert input[name="accept_name"]').send_keys("小狗")
    # 定位省市区下拉框
    driver.find_element_by_css_selector('.__address_alert [name="province"]').click()
    # 选择上海市
    driver.find_element_by_css_selector('option[value="310000"]').click()
    # 选择市辖区
    driver.find_element_by_css_selector('.__address_alert [name="city"]').click()
    # 选择选择市
    driver.find_element_by_css_selector('option[value="310100"]').click()
    # 选择区
    driver.find_element_by_css_selector('.__address_alert [name="area"]').click()
    # 选择杨浦
    driver.find_element_by_css_selector('option[value="310110"]').click()
    time.sleep(1)
    # 填写地址
    driver.find_element_by_css_selector('input[class="__text"][name="address"]').send_keys("五角场")
    # 填写手机号
    driver.find_element_by_css_selector('input[class="__text"][name="mobile"]').send_keys("15574822111")
    # 填写固定电话
    driver.find_element_by_css_selector('input[class="__text"][name="telphone"]').send_keys("0731-00009")
    # 填写邮编
    driver.find_element_by_css_selector('input[class="__text"][name="zip"]').send_keys("400031")
    # 跳出框架
    driver.switch_to.default_content()
    # 点击浮窗提交
    driver.find_element_by_css_selector('button[class=" aui_state_highlight"]').click()

    # 选择新增的地址
    add_list = driver.find_elements_by_css_selector('ul[class="addr_list"][id="addr_list"]')
    add_list[0].click()

    # 下拉悬浮框
    driver.execute_script('window.scrollBy(0,5000)')
    # 点击结算按钮
    driver.find_element_by_css_selector(".cart_topay_btn").click()
    # 点击去支付
    driver.find_element_by_xpath("/html/body/div[3]/section[2]/div/form/label/span").click()
    driver.find_element_by_xpath(
        '/html/body/div[1]/div/table/tbody/tr[2]/td[2]/div/table/tbody/tr[3]/td/div/button[1]').click()

    # 切换到支付成功的页面
    new_handles = driver.window_handles
    for n in new_handles:  # 遍历句柄列表
        if n != hadels:
            driver.switch_to.window(n)
    driver.get_screenshot_as_file("../支付成功.png")

    time.sleep(3)

    driver.quit()


Addcart()
