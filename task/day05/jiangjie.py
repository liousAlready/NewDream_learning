#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: jiangjie.py
@time: 2021/4/21 20:10
'''

# # 2、实现输入文件名称，删除文件的一个函数，如果没有文件，则提示文件不存在
#
# import os
#
#
# def deffile(filename):
#     if os.path.isfile(filename):
#         os.remove(filename)
#         print("删除文件成功")
#     else:
#         print("文件不存在")
#
#
# filename = "stuinfo.txt"
# deffile(filename)

# # 3、创建文件夹，文件夹的名称为时分秒，每隔20秒创建一个，共建立10个
# import time
# import os
#
# for i in range(1, 11, 1):
#     dname = time.strftime("%H_%M_%S")
#     time.sleep(2)
#     os.mkdir(dname)

# 4、新建文件 stuinfo.txt,增加学生信息：
'''
新建文件
open() ---w+
writelines() ---list
seek()
readlines()
'''
fp = open("stuinfo.txt", "w+", encoding="utf-8")
slist = ['1 Tom\n', '2 Jerry\n', '3 Lily\n', '4 xiaoming\n']
fp.writelines(slist)  # 写入内容到文件中
fp.seek(0, 0)  # 把光标移动到文件的开头
s1 = fp.readlines()
print(s1[:2])
fp.close()

'''
5、有名为username.txt的文件，其内容格式如下
100001 Lily
100002 Tom
，写一个程序，判断该文件中是否存在"alex", 如果没有，则将字符串"alex"添加到该文件末尾，否则提示用户该用户已存在

'''
fp = open("username.txt", "r+")
s2 = fp.readlines()
print(s2)
count = 0
for i in s2:
    if 'alex' in i:
        print("有")
        break
    else:
        count = count + 1  # 做个标记 count 用来统计alex判断了多少次
print("统计count的次数：", count)

if count == len(s2):
    s2.append("10003 alex")
    fp.writelines(s2)
fp.seek(0, 0)
fp.close()
