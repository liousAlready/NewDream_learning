#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day05.py
@time: 2021/4/19 09:08
'''

'''
1、从键盘输入内容到一个文本文件中。并显示文件中的内容
2、实现输入文件名称，删除文件的一个函数，如果没有文件，则提示文件不存在
3、创建文件夹，文件夹的名称为时分秒，每隔20秒创建一个，共建立10个

4、新建文件 stuinfo.txt,增加学生信息：
	1 Tom
	2 Jerry
	3 Lily
	4 xiaoming
把3号和4号的学生信息显示在屏幕
5、有名为username.txt的文件，其内容格式如下
100001 Lily
100002 Tom
，写一个程序，判断该文件中是否存在"alex", 如果没有，则将字符串"alex"添加到该文件末尾，否则提示用户该用户已存在

'''

import os
import time
import datetime

# 1、从键盘输入内容到一个文本文件中。并显示文件中的内容
# 创建一个txt文件
open_txt = open('今晚打老虎.txt', 'w+', encoding="utf-8")
# 将输入进来的字符串定义成c
c = input("请输入小说的内容: \t")
# 写入小说
open_txt.writelines(c)
# 刷新缓存
open_txt.flush()
# 关闭文件
open_txt.close()

# 2、实现输入文件名称，删除文件的一个函数，如果没有文件，则提示文件不存在
filename = '今晚打老虎.txt'


def del_file(file_names):
    if os.path.isfile(file_names):
        print("找到文件了,我把他删除啦！")
        os.remove(file_names)
    else:
        print("文件可能已经被删除了")


del_file(filename)

# 3、创建文件夹，文件夹的名称为时分秒，每隔20秒创建一个，共建立10个
for i in range(1, 11, 1):
    print("=====准备创建文件夹=====")
    time.sleep(1)
    times = datetime.datetime.today()
    file_name = "%s%s%s" % (times.hour, times.minute, times.second)
    if os.path.isdir(file_name):
        print("文件已存在")
    else:
        print("===正在创建文件===")
        os.mkdir(file_name)
        print("===创建完成！===")

# 4、新建文件 stuinfo.txt,增加学生信息：
# 	1 Tom
# 	2 Jerry
# 	3 Lily
# 	4 xiaoming
# 把3号和4号的学生信息显示在屏幕
filename01 = "stuinfo.txt"
with open(filename01, "w+", encoding="utf-8") as stu:
    stu.writelines("1 Tom\n2 Jerry\n3 Lily\n4 xiaoming\n")


def read_file():
    with open(filename01, "r+") as fpp:
        ss = fpp.readlines()
        s_last = ss[-1]
        s_last_second = ss[-2]
        print("三号的信息是", s_last_second)
        print("四号的信息是", s_last)
        fpp.close()


read_file()
'''
5、有名为username.txt的文件，其内容格式如下
100001 Lily
100002 Tom
，写一个程序，判断该文件中是否存在"alex", 如果没有，则将字符串"alex"添加到该文件末尾，否则提示用户该用户已存在
'''

finame = "username.txt"

with open(finame, "w+", encoding="utf-8") as lsp:  # 定义一个文件夹
    lsp.write("100001 Lily \n100002 Tom")  # 插入数据


def insert_name():
    with open(finame, "r+") as reader:  # 打开username 重命名为reader
        ser = reader.read()  # 赋值给ser
        s = "alex"  # 定义s  alex
        if s in ser:
            print("该用户已经存在")
        else:
            print(s, "该用户不存在，现已添加到肯德基豪华午餐！")
            reader.seek(0, 2)
            reader.write("\nalex")  # 如果不存在这个用户则写入
            reader.close()


insert_name()


