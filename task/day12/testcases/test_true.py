#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: test_true.py
@time: 2021/5/24 09:18
'''

from task.day12.comm.createrbrower import Creater
import time
import random


class TestAdd(Creater):
    '''测试购物商场正向用例'''

    def test_Loingt(self):
        '''测试正常登录'''
        self.loginhandle = self.driver.window_handles
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_name("login_info").send_keys("nswe")
        self.driver.find_element_by_name("password").send_keys("111111")
        self.driver.find_element_by_class_name("input_submit").click()
        self.assertIn("nswe", self.driver.find_element_by_css_selector("div.body_toolbar_btn.userinfo a ").text)

    def test_addcart(self):
        '''搜索真皮女包'''
        self.test_Loingt()
        time.sleep(2)
        self.driver.find_element_by_name("word").send_keys("真皮女包")
        self.driver.find_element_by_class_name("search_submit").click()
        self.assertIn("真皮女包", self.driver.title)
        # 点击单个商品
        # self.driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/section/section[2]/ul/li[1]/a/img").click()

        # 在商品列表中选择单个商品
        list1 = self.driver.find_elements_by_css_selector(".goods_list ul li a")
        time.sleep(2)
        add = random.randrange(0, len(list1) - 1)
        list1[add].click()
        self.assertIn("真皮女包",list1[add].text)

    def test_paycart(self):
        '''测试将加入购物车'''
        self.test_addcart()
        # 切句柄
        hadels = self.driver.window_handles
        for n in hadels:  # 遍历句柄列表
            if n != hadels:
                self.driver.switch_to.window(n)
        time.sleep(5)
        add_ca = self.driver.find_element_by_css_selector("#joinCarButton > span")
        self.assertIn("加入购物车", add_ca.text)
        add_ca.click()

    def test_quejiesuan(self):
        '''测试跳转结算页面'''
        self.test_paycart()
        self.driver.find_element_by_xpath('/html/body/header/div[1]/div/div[3]/a').click()
        # 下拉悬浮框
        self.driver.execute_script('window.scrollBy(0,5000)')
        # 点击去结算按钮
        qujiesuan = self.driver.find_element_by_link_text("去结算")
        self.assertIn("去结算", qujiesuan.text)
        qujiesuan.click()

    def test_address(self):
        '''添加收货地址'''
        self.test_quejiesuan()
        # 添加地址
        self.driver.find_element_by_link_text("添加新地址").click()
        # 定位iframe框
        new_yemian = self.driver.find_element_by_xpath('//iframe[starts-with(@name,"OpenaddressWindow")]')
        self.driver.switch_to.frame(new_yemian)
        # 定位到姓名
        name = self.driver.find_element_by_css_selector('.__address_alert input[name="accept_name"]')
        name.send_keys("小狗")
        # 定位省市区下拉框
        self.driver.find_element_by_css_selector('.__address_alert [name="province"]').click()
        # 选择上海市
        self.driver.find_element_by_css_selector('option[value="310000"]').click()
        # 选择市辖区
        self.driver.find_element_by_css_selector('.__address_alert [name="city"]').click()
        # 选择选择市
        self.driver.find_element_by_css_selector('option[value="310100"]').click()
        # 选择区
        self.driver.find_element_by_css_selector('.__address_alert [name="area"]').click()
        # 选择杨浦
        self.driver.find_element_by_css_selector('option[value="310110"]').click()
        time.sleep(1)
        # 填写地址
        self.driver.find_element_by_css_selector('input[class="__text"][name="address"]').send_keys("五角场")
        # 填写手机号
        self.driver.find_element_by_css_selector('input[class="__text"][name="mobile"]').send_keys("15574822111")
        # 填写固定电话
        self.driver.find_element_by_css_selector('input[class="__text"][name="telphone"]').send_keys("0731-00009")
        # 填写邮编
        self.driver.find_element_by_css_selector('input[class="__text"][name="zip"]').send_keys("400031")
        # 跳出框架
        self.driver.switch_to.default_content()
        # 点击浮窗提交
        self.driver.find_element_by_css_selector('button[class=" aui_state_highlight"]').click()
        # 选择新增的地址
        add_list = self.driver.find_elements_by_css_selector('ul[class="addr_list"][id="addr_list"]')
        add_list[0].click()

        # 断言地址添加成功
        self.assertIn("小狗", add_list[0].text)
        # 下拉
        self.driver.execute_script('window.scrollBy(0,5000)')
        # 点击结算按钮
        self.driver.find_element_by_css_selector(".cart_topay_btn").click()
        # 下拉
        self.driver.execute_script('window.scrollBy(0,5000)')
        time.sleep(2)
        try:
            go_pay = self.driver.find_element_by_xpath("/html/body/div[3]/section[2]/div/form/label/span")
            self.assertIn("立即支付", go_pay.text)

        except Exception:
            print("当前订单提交过于频繁，请稍后再试")
        else:
            go_pay.click()

    def test_png(self):
        '''跳转到支付成功页面并截图'''
        self.test_address()
        # 切换到支付成功的页面
        new_handles = self.driver.window_handles
        for n in new_handles:  # 遍历句柄列表
            if n != self.loginhandle:
                self.driver.switch_to.window(n)
        time.sleep(2)
        try:
            tab = self.driver.find_element_by_xpath("/html/body/div[3]/div/section/article/strong")
        except Exception as e:
            print(e)
        else:
            self.assertIn("支付成功", tab.text)
            self.driver.get_screenshot_as_file("../支付成功.png")
