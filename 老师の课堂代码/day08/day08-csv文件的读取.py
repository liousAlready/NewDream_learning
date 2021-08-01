'''
@File : day08-csv文件的读取.py
@Time : 2021/5/9 14:44
@Author: luoman
'''
# import lib
import csv
from 老师の课堂代码.day08.day08_logger import Logging

log = Logging().getloger()


class Readcsv:
    def __init__(self, filename):
        self.filename = filename

    def readcsv(self, filename):
        try:
            self.fp = open(filename, 'r+', encoding='utf-8')
            log.info('正在读取csv文件')
            content = csv.DictReader(self.fp)
            self.list = []
            for c in content:
                if content.line_num == 1:
                    continue
                else:
                    self.list.append(c)
        except Exception:
            print('文件打开失败')
            log.error('文件的打开失败')

        finally:
            self.fp.close()

    def getindex(self, n):
        return self.list[n]['序号']

    def getname(self, n):
        return self.list[n]['名字']

    def getpeoplecount(self, n):
        return self.list[n]['人数']

    def getloads(self, n):
        return self.list[n]['载重']

    def getrents(self, n):
        return self.list[n]['租金']


filename = 'file/car1.csv'
r1 = Readcsv(filename)
r1.readcsv(filename)



print(r1.getindex(2))
print(r1.getrents(1))
