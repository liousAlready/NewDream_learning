'''
@File : day10_selenium3.py
@Time : 2021/5/16 10:57
@Author: luoman
'''
import time

# import lib
from selenium import webdriver


#selenium进行元素识别的方法 --- 7种方法
def demo1():
    driver = webdriver.Chrome()
    #driver.get('http://www.xmxbbs.com')
    driver.get('http://www.baidu.com')
    # 1、通过id方法
    #driver.find_element_by_id('scbar_txt').send_keys('mysql') # send_keys('mysql') 表示要输入的内容
    # 2、通过name方法
    #driver.find_element_by_name('srchtxt').send_keys('python')
    # 3、通过class属性方法:class_name
    #driver.find_element_by_class_name("pn").click()  # click() 表示 点击操作
    # 4、通过标签名 tag_name  用得比较少，标签名的重复度比较高
    time.sleep(1)
    #driver.find_element_by_tag_name('map').click()
    # 5、通过链接文本来进行识本  一定要是a标签上的文本
    driver.find_element_by_link_text('新闻').click()
    driver.find_element_by_partial_link_text('新').click()  # 通过文本的一部分内容进行识别

    time.sleep(3)
# demo1()

# 第6种方法 xpath
# 有6种小方法来找元素

def demo2():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    # 1、绝对路径的方法  必须从html标签开始，以/开头
    #driver.find_element_by_xpath('/html/body/div/div/div[3]/a').click() # 如果同一级别标签名相同，则需要指名下标，下标从1开始
    # 2、相对路径 以//开头
    # driver.find_element_by_xpath('//div/div/div[3]/a').click()
    # 3、元素索引定位 结合相对路径或绝对路径
    # 4、通过元素的属性值进行定位 '//标签名[@属性="属性值"]'
    # 支持使用and 和 or 关键字，多个属性一起定位元素。
    # driver.find_element_by_xpath('//input[@maxlength="255"]').send_keys('selenium')
    # driver.find_element_by_xpath('//input[@maxlength="255" and @id="kw"]').send_keys('selenium')
    # 5、进行模糊匹配--元素的属性值可能是动态变化的  或是太长
    #  元素属性值开头包含内容：starts-with()  元素属性值结尾包含内容：substring()  元素属性值包含内容：contains()
    # driver.find_element_by_xpath('//a[starts-with(@name,"tj_bri")]').click()
    # driver.find_element_by_xpath('//a[substring(@name,7)="icon"]').click() #substring(@name,7) 7表示name属性值中的从第7个字符开始到字符串的末尾
    # driver.find_element_by_xpath('//a[contains(@name,"j_bri")]').click()
    # 6、元素文本定位  通过text()进行获取 不一定只有a标签才有文本
    driver.find_element_by_xpath('//span[text()="国家卫健委派出工作组赴辽宁"]').click()
    driver.find_element_by_xpath('//span[contains(text(),"国家卫健委")]').click()

    time.sleep(2)

# demo2()
# 第7种元素识别的方法：Css_selector
def demo3():
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com')
    # 第1种方法：使用绝对路径 html开始，使用id或者class属性进行标记
    # driver.find_element_by_css_selector('html body div#wrapper div#head div#s-top-left a.c-font-normal').click()
    # 第2种方法：使用相对路径
    # driver.find_element_by_css_selector('div#head div#s-top-left a.c-font-normal').click()
    # 第3种方法：元素属性  标签名[属性="属性值"]
    #driver.find_element_by_css_selector('a[name="tj_briicon"]').click()
    # driver.find_element_by_css_selector('a[name="tj_briicon"][class="s-bri"]').click()
    # 第4种方法：模糊定义：属性值如果太长或网页中的元素属性动态变化
    # $=:以..结束  ^=:以..开头  *=：包含
    # driver.find_element_by_css_selector('a[name^="tj_bri"]').click()
    # driver.find_element_by_css_selector('a[name$="iicon"]').click()
    # driver.find_element_by_css_selector('a[name*="brii"]').click()
    # 第5种方法：查询子元素
    # driver.find_element_by_css_selector('form span input').send_keys('selenium')
    # driver.find_element_by_css_selector('form>span>input').send_keys('selenium')
    # driver.find_element_by_css_selector('div#s-top-left a:first-child').click()
    # driver.find_element_by_css_selector('div#s-top-left a:last-child').click()
    # driver.find_element_by_css_selector('div#s-top-left a:nth-child(3)').click()
    # 第6种方法：查询兄弟元素
    # driver.find_element_by_css_selector('div#s-top-left a+a+a+a').click()
    from selenium.webdriver.common.by import By
    driver.find_element(By.CSS_SELECTOR, 'div#s-top-left a+a+a+a').click()
    time.sleep(2)

demo3()