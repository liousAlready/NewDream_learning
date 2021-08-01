'''
@File : readexcel.py
@Time : 2021/5/15 23:29
@Author: luoman
'''
# import lib
import os
import xlrd
from task.day09.老师的 import student_base_info
from task.day09.老师的.logger import Logging
from task.day09.老师的.send_email import sendemail

log = Logging().getloger()


class Read_excel:

    def __init__(self, excel_path):
        self.excel_path = excel_path

    def read_excel_data(self):
        student_infos = []  # 存储学生对象
        try:
            work_book = xlrd.open_workbook(self.excel_path)
            log.info('打开xlsx文件')
            sheet = work_book.sheet_by_index(0)
            log.info('正在读取表1中的内容')
            for i in range(1, sheet.nrows):  # 包头不包尾，结束值 nrows-1
                # 通过模块名.类名()对学生进行初始化，也就是定义学生对象
                student_info = student_base_info.StudentBaseInfo(sheet.cell_value(i, 0), sheet.cell_value(i, 1),
                                                                 sheet.cell_value(i, 2), sheet.cell_value(i, 3),
                                                                 sheet.cell_value(i, 4)
                                                                 )
                student_infos.append(student_info)
            log.info('已经创建成功学生对象:%d个' % (sheet.nrows - 1))
        except Exception as e:
            log.error('打开xlsx文件失败', e)
        return student_infos


if __name__ == '__main__':
    # 测试代码
    print(__file__)
    current_path = os.path.dirname(__file__)

    excel_path = os.path.join(current_path, 'student.xlsx')
    r = Read_excel(excel_path)
    student_infos = r.read_excel_data()
    for stu in student_infos:
        print("学号：%s" % stu.stu_id)
        print("姓名：%s" % stu.stu_name)
        print("性别：%s" % stu.stu_sex)
        print("年龄：%s" % stu.stu_age)
        print("分数：%d" % stu.stu_score)
        print("------------------------")
    filename = Logging().getlogname()
    print(filename)
    sendemail(filename)
