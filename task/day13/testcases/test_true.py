#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: test_true.py
@time: 2021/5/24 09:18
'''

from task.day13.comm.createrbrower import CreaterBrower
import time
from selenium.webdriver.common.by import By
from task.day13.PageObject.login_page import LoginPage as login

class Testtrue(CreaterBrower):
    '''测试购物商场正向用例'''

    def test_Loingt(self):
        '''测试正常登录'''
        # self.bo.logins("nswe", "111111", By.LINK_TEXT, "登录")
        self.bo.logins("nswe", "111111")
        #self.assertIn("nswe", self.driver.find_element_by_css_selector("div.body_toolbar_btn.userinfo a ").text)

    # def test_search(self):
    #     '''测试搜索真皮女包'''
    #     self.test_Loingt()
    #     self.bo.search(By.NAME, "word", "真皮女包")
    #     # 断言标题是否为真皮女包
    #     self.assertIn("真皮女包", self.driver.title)
    #
    # def test_select(self):
    #     '''测试选择商品'''
    #     # 搜索商品
    #     self.test_search()
    #     # 点击单个商品
    #     time.sleep(2)
    #     self.bo.select_sp(By.XPATH, "/html/body/div[3]/div/section[2]/section/section[2]/ul/li[1]/a/img")
    #     time.sleep(2)
    #     # 断言不了,需要切换句柄到下一个窗口
    #     self.bo.swtihwindows()
    #     # 断言跳转窗口是否为真皮女包
    #     self.assertIn('真皮女包', self.driver.find_element_by_xpath("/html/body/div[3]/div/section[2]/section[2]/h1").text)
    #
    # def test_paycart(self):
    #     '''测试将加入购物车'''
    #     self.test_select()
    #     # 不用切句柄跳转页面，上个用例已经做判断了
    #     time.sleep(2)
    #     # 点击加入购物车
    #     self.bo.add_cart(By.CSS_SELECTOR, "#joinCarButton > span")
    #     # 断言是否到添加购物车界面
    #     self.assertIn("加入购物车", self.driver.find_element_by_css_selector("#joinCarButton > span").text)
    #
    # def test_qjs(self):
    #     '''测试跳转结算页面'''
    #     self.test_paycart()
    #     # 点击跳转结算页面
    #     self.bo.clickr(By.XPATH, "/html/body/header/div[1]/div/div[3]/a")
    #     # 下拉悬浮框
    #     self.bo.teardownwindow()
    #     # 点击去结算按钮
    #     self.bo.clickr(By.LINK_TEXT, "去结算")
    #     # 断言是否跳转到添加地址页面
    #     self.assertIn("收货人信息", self.driver.find_element_by_xpath('//*[@id="addressBox"]/h3').text)
    #
    # def test_address(self):
    #     '''添加收货地址'''
    #     self.test_qjs()
    #     # 添加地址
    #     dress = "添加新地址"
    #     self.bo.clickr(By.LINK_TEXT, dress)
    #     # # 定位iframe框
    #     self.bo.tabiframe(By.XPATH, '//iframe[starts-with(@name,"OpenaddressWindow")]')
    #     # 输入姓名
    #     time.sleep(2)
    #     self.bo.inputd(By.CSS_SELECTOR, '.__address_alert input[name="accept_name"]', "tiango")
    #     # 定位省市区下拉框
    #     self.bo.clickr(By.CSS_SELECTOR, '.__address_alert [name="province"]')
    #     # 选择上海市
    #     self.bo.clickr(By.CSS_SELECTOR, 'option[value="310000"]')
    #     # 选择市辖区
    #     self.bo.clickr(By.CSS_SELECTOR, '.__address_alert [name="city"]')
    #     # 选择选择市
    #     self.bo.clickr(By.CSS_SELECTOR, 'option[value="310100"]')
    #     # 选择区
    #     self.bo.clickr(By.CSS_SELECTOR, '.__address_alert [name="area"]')
    #     # 选择杨浦
    #     self.bo.clickr(By.CSS_SELECTOR, 'option[value="310110"]')
    #     time.sleep(2)
    #     # # 填写地址
    #     self.bo.inputd(By.XPATH, '/html/body/form/section/ul/li[3]/input', "五角场")
    #     # # 填写手机号
    #     self.bo.inputd(By.XPATH, '/html/body/form/section/ul/li[4]/input', "15574928812")
    #     # # 填写固定电话
    #     self.bo.inputd(By.XPATH, '/html/body/form/section/ul/li[5]/input', "0731-00009")
    #     # # 填写邮编
    #     self.bo.inputd(By.XPATH, '/html/body/form/section/ul/li[6]/input', "400031")
    #     # 跳出框架
    #     self.bo.tabiframeto()
    #     # 点击浮窗提交
    #     self.bo.clickr(By.CSS_SELECTOR, 'button[class=" aui_state_highlight"]')
    #     time.sleep(2)
    #     # 选择新增的地址
    #     self.bo.addresslist(By.CSS_SELECTOR, 'ul[class="addr_list"][id="addr_list"]')
    #     # 断言地址添加成功
    #     self.assertIn("tiango", self.driver.find_element_by_xpath('//*[@id="addressBox"]').text)
    #
    # def test_pay(self):
    #     self.test_address()
    #     # 下拉
    #     self.bo.teardownwindow()
    #     # 点击结算按钮
    #     self.bo.clickr(By.CSS_SELECTOR, ".cart_topay_btn")
    #     # 下拉
    #     self.bo.teardownwindow()
    #     time.sleep(2)
    #     try:
    #         self.assertIn("立即支付",
    #                       self.driver.find_element_by_xpath("/html/body/div[3]/section[2]/div/form/label/span").text)
    #     except Exception:
    #         print("当前订单提交过于频繁，请稍后再试")
    #     else:
    #         self.bo.clickr(By.XPATH, '/html/body/div[3]/section[2]/div/form/label/span')
    #
    # # def test_png(self):
    # #     '''跳转到支付成功页面并截图'''
    # #     self.test_address()
    # #     # 切换到支付成功的页面
    # #     new_handles = self.driver.window_handles
    # #     for n in new_handles:  # 遍历句柄列表
    # #         if n != self.loginhandle:
    # #             self.driver.switch_to.window(n)
    # #     time.sleep(2)
    # #     try:
    # #         tab = self.driver.find_element_by_xpath("/html/body/div[3]/div/section/article/strong")
    # #     except Exception as e:
    # #         print(e)
    # #     else:
    # #         self.assertIn("支付成功", tab.text)
    # #         self.driver.get_screenshot_as_file("../支付成功.png")
