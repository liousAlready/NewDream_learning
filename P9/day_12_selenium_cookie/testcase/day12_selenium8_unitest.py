#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: baidusearch.py
@time: 2021/5/23 09:37
'''

'''
1.代码的重复率高
2.可扩展性、维护性不强
3.数据和代码是放在一起的

公司对代码的要求：
    1、使用和实现分开
    2、数据和代码分离
    3、高内聚，低耦合
'''

# 可以使用框架进行使用 ---写代码的难度就会降低
# 基于第三方或者系统提供的框架，然后在这个框架的基础上加上自己要实现的功能
# 功能：根据业务能够执行多条用例，日志记录，数据保存在文件中，生成测试报告，邮件提醒，用例的重跑，断言
# 就可以实现：公共功能保持不变，只需要修改与业务相关的部分

'''
测试百度首页进行部分功能的测试：
1.搜索框： a、测试正常的关键--python b、测试关键字中包含特殊符号 c、没有输入关键字
2.测试链接：新闻，hao123，地图...

'''

'''
有了unittest环境之后就会有两形式执行.py文件
一种是用python环境执行
一种是用unittest环境执行

'''
# 1.引入unittest
import unittest
from selenium import webdriver
import time
from P9.comm import creatbrower


# 2.让所有执行测试的类都继承于TestCase类,可以将TestCase看成是对特定类进行测试的方法的集合
# setUp()方法中进行测试前的初始化工作，teardown()方法中执行测试后的清除工作，它们都是TestCase中的方法
# 4.编写测试的方法最好以test开头（可以直接运行）deftest_add(self)、deftest_sub(self)等，可以编写多个测试用例对被测对象进行测试
# e)在编写测试方法过程中，使用TestCaseclass提供的方法测试功能点，比如：assertEqual等f)调用unittest.main()方法运行所有以test开头的方法
version = '1.3'


class TestBaidu(creatbrower.CreaterBrowser):
    '''测试百度的测试用例'''

    # # 初始化
    # def setUp(self):  # 定义一次 自动调用，每一次执行测试用例之前都会调用setUp()
    #     print("操作之前")
    #     self.driver = webdriver.Chrome()
    #     self.driver.get("http://www.baidu.com")
    #     self.handle = self.driver.current_window_handle
    #
    # # 执行测试后的清除工作
    # def tearDown(self):  # 定义一次 自动调用，每一次执行测试用例之后都会调用tearDown()
    #     print("操作之后")
    #     self.driver.quit()

    def test_serch1(self):
        '''测试正常功能的用例'''
        self.driver.find_element_by_id("kw").send_keys("python")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertIn('python', self.driver.title)

    @unittest.skip("该用例对应的功能已经被删除")
    def test_serch2(self):
        '''测试包含特殊字符的用例'''
        self.driver.find_element_by_id("kw").send_keys("python??")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertIn('python', self.driver.title)

    # @unittest.skipIf(version == "1.3","1.3版本不执行该用例")
    @unittest.skipUnless(version == '1.3', "false的时候跳过这条用例")
    @unittest.expectedFailure
    def test_serch3(self):
        '''测试不输入内容的测试用例'''

        self.driver.find_element_by_id("kw").send_keys("python")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertIn('百度一下', self.driver.title)


'''
测试套件：测试用例集合---把自己需要执行的用例装载到测试套件中
'''

'''
使用skip装饰器，对用例进行进一步管理
'''

# 在类的外面写
# 方法一：
# # 定义一个测试套件的对象
# suite = unittest.TestSuite()
# # 把用例装载到条件中
# suite.addTest(TestBaidu('test_serch1'))
# suite.addTest(TestBaidu('test_serch3'))
# unittest.main(defaultTest='suite')

# 方法二：
# def createsuite():
#     # 定义一个测试套件的对象
#     suite = unittest.TestSuite()
#     # 把用例装载到条件中
#     suite.addTest(TestBaidu('test_serch1'))
#     suite.addTest(TestBaidu('test_serch2'))
#     suite.addTest(TestBaidu('test_serch3'))
#     return suite
# unittest.main(defaultTest='suite')

# # 方法三:
# def createsuite_A():
#     # 先定义列表写好用例的名字
#     tests = ['test_serch1', 'test_serch2']
#     return unittest.TestSuite(map(TestBaidu, tests))
#
#
# if __name__ == '__main__':
#     unittest.main(defaultTest='createsuite_A')
