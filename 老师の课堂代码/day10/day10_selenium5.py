'''
@File : day10_selenium5.py
@Time : 2021/5/16 16:10
@Author: luoman
'''
# import lib

from selenium import webdriver
import time
# 场景的处理
# 一 、 等待处理：为了保证脚本的稳定性，有时候需要引入等待时间，等待页面加载元素后再进行操作
# selenium提供三种等待时间设置方式：1、固定等待 2、隐式等待 3、显示等待

# 固定等待: time.sleep() 设置多长时间，就必须等待多长时间 10s

# 隐式等待: implicitly_Wait(); 比固定等待要灵活，只要在规定的时间内，元素就被找到的话，那么就不再等待
#          全局等待：从隐式等待设置的位置开始往后进行元素识别时，每一次都会去启动等待

# 显示等待：WebDriverWait(): 等待某一个条件满足，那就不再等待了，否则抛出异常
#  不是全局等待，每一条件都需要设置等待

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def demo8():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    driver.implicitly_wait(10)  # 隐式等待10s,只要元素被识别到，就不再等.如果元素无法找到，则需要一直等待，只到时间结束抛出异常
    # 假设直到页面标题包含'百度一下',才进行下一步操作
    # WebDriverWait(driver, 10, 0.5).until(EC.title_contains('百度一下'))
    # WebDriverWait(driver, 10, 0.5).until(EC.title_contains('p9')) # 抛出异常的案件

    driver.find_element_by_id('kw').send_keys('java')
    # driver.find_element_by_id('kwkwkwkw').send_keys('java')

    time.sleep(2)


# demo8()

# 二、识别一组元素 --通过某一个共同的属性及属性值，找到所有的元素
import random
def demo9():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    # 识别出所有a标签 存入到一个列表
    # list1  = driver.find_elements_by_tag_name('a')
    # print(len(list1))
    list2 = driver.find_elements_by_class_name('mnav')  # 返回的是列表
    print(len(list2))
    r = random.randint(0, len(list2)-1)
    list2[r].click()
    time.sleep(2)

# demo9()
# 多窗口切换：窗口句柄---唯一标识窗口的字符串
'''
# 当页面因为某个元素的操作新打开一个标签页面，但是driver还留在原来的标签页
    # 此时如果需要在新的标签页进行操作的话，就必须把driver跳到新的标签页---窗口句柄
1、打开第一个页面后，获取第一个页面的窗口句柄
2、打开新的页面
3、获取两个页面的窗口句柄
4、通过对窗口句柄进行判断，跳转到新的窗口，然后继续进行操作
'''
def demo10():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('http://www.baidu.com')
    # 1、打开第一个页面后，获取第一个页面的窗口句柄
    handle = driver.current_window_handle
    print(handle)
    # 2、打开新的页面
    driver.find_element_by_link_text('新闻').click()
    # 3、获取两个页面的窗口句柄
    handles = driver.window_handles
    print(handles)
    # 4、通过对窗口句柄进行判断，跳转到新的窗口，然后继续进行操作
    for h in handles:
        if h !=handle:
            driver.switch_to.window(h)
    time.sleep(2)
    driver.find_element_by_link_text('国际').click()
    # 假设在新的窗口上操作完成，需要返回到原来的窗口
    driver.switch_to.window(handle)
    time.sleep(2)
demo10()

