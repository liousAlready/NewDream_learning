'''
@File : browseroperator.py
@Time : 2021/5/26 20:27
@Author: luoman
'''
# import lib

from 老师の课堂代码.baidu_selenium_demo.comm.logger import log


class BrowserOperator:

    def __init__(self, driver):
        self.driver = driver

    # 第二个地方改进的
    # 第三个地方是加入日志，日志是会打印两次，请问该如何解决？

    # 切换窗口的函数
    def switchwindow(self, type, type_value):  # type：表示元素识别的方法，type_value:方法的值
        log.info('进行窗口切换')
        self.handle = self.driver.current_window_handle
        self.driver.find_element(type, type_value).click()
        self.handles = self.driver.window_handles
        for h in self.handles:
            if h != self.handle:
                self.driver.switch_to.window(h)

    # 最大化
    def set_window_max(self):
        log.info('窗口进行最大化')
        self.driver.maximize_window()

    # 第二章的浏览器操作API 请写在这个页面
    def refresh_window(self):
        log.info('刷新浏览器')
        self.driver.refresh()

    def get_url(self, url):
        log.info('打开页面:%s' % url)
        self.driver.get(url)
