'''
@File : config.py
@Time : 2021/6/30 21:01
@Author: luoman
'''
# import lib
import configparser
class Config:
    def __init__(self):
        self.configpath = '/Users/luoman/python_code/p9_code/baidu_selenium_demo/conf/conf.ini'  # .ini文件的路径
        self.conf = configparser.ConfigParser()  # 定义读取.ini文件的对象

        self.conf.read(self.configpath, encoding='utf-8')
        # print(conf.sections()) # 获取所有sections

        self.url = self.conf.get('host', 'host')
