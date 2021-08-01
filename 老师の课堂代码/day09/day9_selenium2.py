'''
@File : day9_selenium2.py
@Time : 2021/5/12 20:56
@Author: luoman
'''
# import lib
# selenium 操作浏览器
from selenium import webdriver

import time

def cdriver():
    driver = webdriver.Chrome() # 打开浏览器
    # 输入网址
    driver.get('http://www.xmxbbs.com')
    # 最大化窗口
    # driver.maximize_window()
    # 设置窗口的大小
    driver.set_window_size(500,600) # 单位是像素
    # 刷新浏览器
    driver.refresh()
    # 后退一步
    time.sleep(2)
    #driver.back()
    # 前进一步
    time.sleep(2)
    #driver.forward()

    # 获取浏览器的内容：
    # 获取页面的标题
    title = driver.title
    print('当前页面的标题是:',title)
    # 获取页面的url
    url = driver.current_url
    print('当前页面的url是:', url)
    # 获取页面的源代码
    pagesource = driver.page_source
    print('当前页面的源代码是:', pagesource)
    if '百度' not in title:
        # 截图
        driver.get_screenshot_as_file('../file/xmx.png')
        raise Exception('打开失败')
    # 关闭浏览器
    # 关闭页签
    driver.close()
    # 退出浏览器--退出浏览器驱动
    driver.quit()  # 请尽量写这一句   chromedriver.exe


try:
    cdriver()
except Exception as exc:
    print(exc)
