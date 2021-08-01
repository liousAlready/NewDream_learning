'''
@File : day10_selenium4.py
@Time : 2021/5/16 14:51
@Author: luoman
'''
# import lib
from selenium import webdriver
import time
# 常用元素操作API
def demo4():
    driver = webdriver.Chrome()
    #driver.get('http://www.xmxbbs.com')
    driver.get('http://www.baidu.com')
    # clear() 清除元素中的内容：建议在输入框中有默认值的时候进行使用，先把默认值清除再输入数据
    driver.find_element_by_id('kw').send_keys('java')
    time.sleep(3)
    driver.find_element_by_id('kw').clear()
    time.sleep(3)
    '''
    submit() : 提交表单，要求对象必须是表单,父标签必须是form
    driver.find_element(By.ID,'form').submit()  
    '''
# demo4()
def demo5():
    driver = webdriver.Chrome()

    driver.get('https://www.12306.cn/index/')
    # 获取元素的尺寸
    e = driver.find_element_by_id('fromStationText')
    size = e.size
    print('尺寸:',size)
    # 获取元素的坐标 坐标原点(0,0)是屏幕的左上角
    loction = e.location
    print('坐标：', loction)
    e1 = driver.find_element_by_class_name('form-label')
    print('文本', e1.text)
    # 是否被选中
    e2 = driver.find_element_by_id('isStudentDan')
    print('是否被选中前', e2.is_selected())
    e2.click()
    time.sleep(2)
    print('是否可见', e2.is_displayed())
    print('是否可用', e2.is_enabled())
    print('获取标签名',e2.tag_name)

    print('获取属性值',e.get_attribute('type'))
    print('获取出发日期的readonly的值',driver.find_element_by_id('train_date').get_attribute('readonly'))
# demo5()

# 鼠标和键盘操作
#  鼠标：单击鼠标 双击鼠标 右击鼠标，拖动鼠标，把鼠标放在某个元素上面
from selenium.webdriver.common.action_chains import ActionChains
def demo6():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    # 右击鼠标
    # 1、先要定义鼠标对象
    mouse = ActionChains(driver)
    # 2、识别元素
    e = driver.find_element_by_id('kw')
    # 3、在元素上进行鼠标操作
    mouse.context_click(e).perform() # perform()执行鼠标操作
    time.sleep(2)
    mouse.release(e).perform()
    time.sleep(3)
    # 把鼠标放到某一个元素上
    e1 = driver.find_element_by_name('tj_briicon')
    mouse.move_to_element(e1).perform()
    time.sleep(3)

# demo6()
'''
键盘上键是有分类：分为普通按键和修饰键(alt,ctrl,shift---key_up()和key_down())
所有的按键由keys()类提供

'''
from selenium.webdriver.common.keys import Keys
def demo7():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    e = driver.find_element_by_id('kw')
    e.send_keys('javaaaa')
    time.sleep(2)
    # e.send_keys(Keys.BACKSPACE)
    time.sleep(2)
    # e.send_keys(Keys.TAB)
    # time.sleep(2)
    # ctrl+a ctrl+c ctrl+v
    # 先创建键盘对象
    k = ActionChains(driver)
    k.key_down(Keys.CONTROL).send_keys('c').key_up(Keys.CONTROL).perform()
    k.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(3)

demo7()
