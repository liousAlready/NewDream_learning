'''
@File : day12_selenium7.py
@Time : 2021/5/23 08:34
@Author: luoman
'''
# import lib

# cookie处理：
'''
cookie: 用来存储用户信息
'''
from selenium import webdriver
import time

def demo17():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://www.baidu.com')

    # 获取所有cookies
    print(driver.get_cookies())  # 以列表的形式返回
    for c in driver.get_cookies():
        print(c)

    # 获取某一项cookie
    print('删除前。。。', driver.get_cookie('BAIDUID'))

    # 删除cookie
    driver.delete_cookie('BAIDUID')

    print('删除后..', driver.get_cookie('BAIDUID'))

    # 添加cookie,必须以字典的形式添加
    driver.add_cookie({'domain': '.baidu.com', 'expiry': 1653266678.73841, 'httpOnly': False, 'name': 'BAIDUID', 'path': '/', 'secure': False, 'value': 'DFA784CFC6F257469276FBF26A458494:FG=1'}
)

    print('添加后..', driver.get_cookie('BAIDUID'))


# demo17()

# 验证码处理
# 分类：1、图片验证码  2、短信验证码  -- 作用：都是为了安全，人机校验
#      3、动态验证 (实名认证的时候)  -- 作用：活体较验
'''
使用UI自动化如何实现验证码操作：
1、设置万能验证码 
2、不对验证码进行校验
3、去掉验证码
4、cookie进行登陆时的绕过验证码
5、图片验证码--使用python代码进行验证码识别，或者自己写算法 识别 --- 成功率不高
6、或者是由开发配合，能否通过接口或者其它方式 获取验证码
'''

def demo18():
    # 先获取正常登陆下的cookie信息
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://shop.aircheng.com/simple/login')
    driver.delete_all_cookies()
    time.sleep(2)
    driver.find_element_by_name('login_info').send_keys('nswe')
    driver.find_element_by_name('password').send_keys('111111')
    time.sleep(2)
    driver.find_element_by_class_name('input_submit').click()
    time.sleep(2)

    # 获取cookies

    cookies = driver.get_cookies()

    for c in cookies:
        print(c)

# demo18()

def demo19():
    # 先获取正常登陆下的cookie信息
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('http://shop.aircheng.com')
    driver.delete_all_cookies() # 删除所有的cookies
    # 一般把cookie存放在文件中

    # cookies = [
    #     {'domain': 'shop.aircheng.com', 'expiry': 1622337090.957763, 'httpOnly': False, 'name': 'iweb_last_login',
    #      'path': '/', 'secure': False,
    #      'value': '2259129a49511cf77aU1ZUUlEBAVYHBVZRAgZUXgQGUFZXBFFRAF1eBAMFXA1WBgMDGQcEHAIDFVUKDAkCCwEN'},
    #     {'domain': 'shop.aircheng.com', 'expiry': 1622337090.957737, 'httpOnly': False, 'name': 'iweb_head_ico',
    #      'path': '/', 'secure': False, 'value': '66f8a52c267973a589BlUDUQFTBVJVVgVTBlUJAAMEBFBUWFRbXgMDVVsFXlU'},
    #     {'domain': 'shop.aircheng.com', 'expiry': 1622337090.957687, 'httpOnly': False, 'name': 'iweb_username',
    #      'path': '/', 'secure': False, 'value': 'fdc1944369fa66ef02UQQCAgMCCABRVAcBVAFTX1gFVA0EB1FQU1NRCVpQAgcIEkRT'},
    #     {'domain': 'shop.aircheng.com', 'expiry': 1622337090.957656, 'httpOnly': False, 'name': 'iweb_user_id',
    #      'path': '/', 'secure': False, 'value': '9115a44eb4e98578a4AVEEB1NTUgMCVAQDUQMAV1pUUVoKAVQAAAsHAlFQBwQN'},
    #     {'domain': 'shop.aircheng.com', 'expiry': 1622337090.957714, 'httpOnly': False, 'name': 'iweb_user_pwd',
    #      'path': '/', 'secure': False,
    #      'value': 'b16badf642964e034bAgQCVQZVUgMAB1IBDVRaAlNTBQZTBwJXAQZUAlIOAAEJAVEAW1ZUWQwHVgFXAQpRCQRYAgIOVwEDUQYAVQRSCw'},
    #     {'domain': 'shop.aircheng.com', 'httpOnly': False, 'name': 'PHPSESSID', 'path': '/', 'secure': False,
    #      'value': 'holbk1qifk43nut26tkgj5imf3'}
    # ]

    # for c in cookies:
    #     driver.add_cookie(c)

    cookies = {'iweb_last_login': '2259129a49511cf77aU1ZUUlEBAVYHBVZRAgZUXgQGUFZXBFFRAF1eBAMFXA1WBgMDGQcEHAIDFVUKDAkCCwEN',
               'iweb_head_ico': '66f8a52c267973a589BlUDUQFTBVJVVgVTBlUJAAMEBFBUWFRbXgMDVVsFXlU',
               'iweb_username': 'fdc1944369fa66ef02UQQCAgMCCABRVAcBVAFTX1gFVA0EB1FQU1NRCVpQAgcIEkRT',
               'iweb_user_id': '9115a44eb4e98578a4AVEEB1NTUgMCVAQDUQMAV1pUUVoKAVQAAAsHAlFQBwQN',
               'iweb_user_pwd': 'b16badf642964e034bAgQCVQZVUgMAB1IBDVRaAlNTBQZTBwJXAQZUAlIOAAEJAVEAW1ZUWQwHVgFXAQpRCQRYAgIOVwEDUQYAVQRSCw',
               'PHPSESSID': 'holbk1qifk43nut26tkgj5imf3'
               }


    for name,value in cookies.items():
        cookie = {'domain': 'shop.aircheng.com',
                  'expiry': 1622337090.957763,
                  'httpOnly': False,
                  'name': name,
                  'path': '/', 'secure': False,
                  'value': value
        }
        driver.add_cookie(cookie)

    time.sleep(4)
    driver.refresh()
    time.sleep(5)

# demo19()

# 上传文件
def demo20():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get('file:///Users/luoman/file/element_samples.html')
    # 只要把文件的路径写入到send_keys中就可以了
    driver.find_element_by_name('attach[]').send_keys('/Users/luoman/file/first.html')

    time.sleep(6)

demo20()