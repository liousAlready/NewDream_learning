#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day12_selenium7.py
@time: 2021/5/23 08:42
'''

# 映入第三库
from selenium import webdriver
from time import sleep


def demo17():
    driver = webdriver.Chrome()
    driver.get("http://www.baidu.com")
    driver.implicitly_wait(30)

    # 获取所有的cookies
    print(driver.get_cookies())  # 以列表的形式返回
    for c in driver.get_cookies():
        print(c)

    # 获取某一项cookies
    print("删除前", driver.get_cookie("BAIDUID"))

    # 删除某一项cookies
    driver.delete_cookie(("BAIDUID"))
    print("删除后", driver.get_cookie("BAIDUID"))

    # 添加cookies
    driver.add_cookie({[
        {'domain': '.baidu.com', 'expiry': 1621734343, 'httpOnly': False, 'name': 'BA_HECTOR', 'path': '/',
         'secure': False, 'value': '2c042l8k042020c0l91gaj9dn0q'},
        {'domain': '.baidu.com', 'httpOnly': False, 'name': 'H_PS_PSSID', 'path': '/', 'secure': False,
         'value': '33799_31660_34004_33607_26350'},
        {'domain': 'www.baidu.com', 'expiry': 1621730743, 'httpOnly': False, 'name': 'BD_LAST_QID', 'path': '/',
         'secure': False, 'value': '12976033710978793753'},
        {'domain': '.baidu.com', 'expiry': 1653266742, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/',
         'secure': False, 'value': 'AD2BEAF119DC0CC11E844D126280C22F:FG=1'},
        {'domain': '.baidu.com', 'expiry': 3769214389, 'httpOnly': False, 'name': 'BIDUPSID', 'path': '/',
         'secure': False, 'value': 'AD2BEAF119DC0CC1F840C4F4355BDE6C'},
        {'domain': '.baidu.com', 'expiry': 3769214389, 'httpOnly': False, 'name': 'PSTM', 'path': '/', 'secure': False,
         'value': '1621730742'},
        {'domain': 'www.baidu.com', 'expiry': 1622594743, 'httpOnly': False, 'name': 'BD_UPN', 'path': '/',
         'secure': False, 'value': '123253'},
        {'domain': 'www.baidu.com', 'httpOnly': False, 'name': 'BD_HOME', 'path': '/', 'secure': False, 'value': '1'}]})

    print('添加后，，', driver.get_cookie("BAIDUID"))

    driver.quit()


# demo17()

# 验证码处理
# 分类：1、图片验证码  2、短信验证码    --作用：都是为了安全，人机校验
#      3、动态验证（实名认证）        --作用：活体校验

'''
使用UI自动化如何实现验证码操作：
1.设置万能验证码
2.不对验证码进行校验
3.去掉验证码
4.cookie进行登录时熬过验证码
5.图片验证码--使用python代码进行识别，或者自己写算法 识别
6.或者是由开发配合，能否通过接口或者其他方式 获取验证码


账号：nswe 密码：111111
'''


def demo18():
    driver = webdriver.Chrome()
    driver.get("http://shop.aircheng.com/")
    driver.delete_all_cookies()
    driver.implicitly_wait(30)

    # 获取正常登录的cookie信息
    # 登录
    login = driver.find_element_by_link_text("登录")
    login.click()
    user_name = driver.find_element_by_name("login_info")
    # 输入用户
    user_name.send_keys("nswe")
    # 定位密码
    user_password = driver.find_element_by_name("password")
    # 输入密码
    user_password.send_keys("111111")
    # 点击登录
    driver.find_element_by_class_name("input_submit").click()
    sleep(5)
    cookie = driver.get_cookies()
    for i in cookie:
        print(i)
    driver.quit()


# demo18()

# 绕过登录
def demo19():
    driver = webdriver.Chrome()
    driver.get("http://shop.aircheng.com/")
    driver.delete_all_cookies()  # 删除所有的cookies
    driver.implicitly_wait(30)

    # cookies = [
    #     {'domain': 'shop.aircheng.com', 'expiry': 1622337107, 'httpOnly': False, 'name': 'iweb_last_login', 'path': '/',
    #      'secure': False,
    #      'value': '208c2b5887d7de5546VFUAAgJUVQkBBlRTUFsAAAVXBFBeUQNaAwdUVAULVAYDCAMHS1EEFAdWFAgJXgcGCVcH'},
    #     {'domain': 'shop.aircheng.com', 'expiry': 1622337107, 'httpOnly': False, 'name': 'iweb_head_ico', 'path': '/',
    #      'secure': False, 'value': 'df458edcf5a7577db9UwUDCFJUCVQBBwZSAQcFWVAEUwUFXAMLUFEAUlAEAAA'},
    #     {'domain': 'shop.aircheng.com', 'expiry': 1622337107, 'httpOnly': False, 'name': 'iweb_username', 'path': '/',
    #      'secure': False, 'value': 'd32d5861bb926fe174BwZTAwlSBlEBCQIABlECDQVSU1YFXVMHVQNWD1tcAQ5fREFd'},
    #     {'domain': 'shop.aircheng.com', 'expiry': 1622337107, 'httpOnly': False, 'name': 'iweb_user_id', 'path': '/',
    #      'secure': False, 'value': '9b263aefc65559ad3bUQFTVlQDBFNTAlEAAwdQBgEDVQEGBVBQAF0GU1IAVwNd'},
    #     {'domain': 'shop.aircheng.com', 'expiry': 1622337107, 'httpOnly': False, 'name': 'iweb_callback', 'path': '/',
    #      'secure': False, 'value': '19fef9d3d06bfcc725BVEAUQcIVQNUBwZTVgMAUwBTAgQLCFYOVFQGCAMDBwA'},
    #     {'domain': 'shop.aircheng.com', 'expiry': 1622337107, 'httpOnly': False, 'name': 'iweb_user_pwd', 'path': '/',
    #      'secure': False,
    #      'value': 'a90b8e43af6f386484AAQHBgEEBFRTBwBXUVVRBQACAw1XUFdUBlZRDwIJUgUNBwRTXQBXCQBUUwABUwRWDgUDUAABXVdUUQAGAQFUAw'}
    #     ]

    # for a in cookies:
    #     driver.add_cookie(a)

    cookiesx = {
        "iweb_last_login": "208c2b5887d7de5546VFUAAgJUVQkBBlRTUFsAAAVXBFBeUQNaAwdUVAULVAYDCAMHS1EEFAdWFAgJXgcGCVcH",
        "iweb_head_ico": "df458edcf5a7577db9UwUDCFJUCVQBBwZSAQcFWVAEUwUFXAMLUFEAUlAEAAA",
        "iweb_username": "d32d5861bb926fe174BwZTAwlSBlEBCQIABlECDQVSU1YFXVMHVQNWD1tcAQ5fREFd",
        "iweb_user_id": "9b263aefc65559ad3bUQFTVlQDBFNTAlEAAwdQBgEDVQEGBVBQAF0GU1IAVwNd",
        "iweb_callback": "19fef9d3d06bfcc725BVEAUQcIVQNUBwZTVgMAUwBTAgQLCFYOVFQGCAMDBwA",
        "iweb_user_pwd": "a90b8e43af6f386484AAQHBgEEBFRTBwBXUVVRBQACAw1XUFdUBlZRDwIJUgUNBwRTXQBXCQBUUwABUwRWDgUDUAABXVdUUQAGAQFUAw", }

    for name, value in cookiesx.items():
        cookie = {'domain': 'shop.aircheng.com',
                  'expiry': 1622337107,
                  'httpOnly': False,
                  'name': name,
                  'path': '/',
                  'secure': False,
                  'value': value}

    driver.add_cookie(cookiesx)

    sleep(5)
    driver.refresh()
    sleep(2)
    driver.quit()


# demo19()

# 上传文件操作
# 绕过登录
def demo20():
    driver = webdriver.Chrome()
    driver.get("file:///Users/lishouwu/Downloads/element_samples.html")
    driver.delete_all_cookies()  # 删除所有的cookies
    driver.implicitly_wait(30)
    # 只要把文件的路径写入send_keys中就可以了
    driver.find_element_by_name("attach[]").send_keys("/Users/lishouwu/Downloads/element_samples.html")

    sleep(3)
    driver.quit()


demo20()
