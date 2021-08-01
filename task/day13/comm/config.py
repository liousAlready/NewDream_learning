'''
@File : config.py
@Time : 2021/5/26 21:24
@Author: luoman
'''
# import lib
import configparser


# ini文件是由sections 和 option组成的

class Config:
    def __init__(self):
        self.configpath = '/Users/lishouwu/PycharmProjects/NewDream_learning/task/day13/conf/conf.ini'  # .ini文件的路径
        self.conf = configparser.ConfigParser()  # 定义读取.ini文件的对象

        self.conf.read(self.configpath, encoding='utf-8')
        # print(conf.sections()) # 获取所有sections
        self.url = self.conf.get('browser', 'url')
        self.browsername = self.conf.get('browser', 'browsername')

        self.casedir = self.conf.get('filepath', 'casedir')
        self.logpath = self.conf.get('filepath', 'logpath')
        self.reportpath = self.conf.get('filepath', 'reportpath')
