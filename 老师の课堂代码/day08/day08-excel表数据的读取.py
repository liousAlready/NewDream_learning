'''
@File : day08-excel表数据的读取.py
@Time : 2021/5/9 14:15
@Author: luoman
'''
# import lib
# excel 的后缀有两个 xls 和 xlsx
# xlrd  读取excel表中的数据
# xlwt  写入数据到excel表中
import xlrd


# 第一步，创建工作簿对象
workbook = xlrd.open_workbook('../file/car.xlsx')
# 第二步，创建表对象
# 方法一：通过表的名字来创建
sheet = workbook.sheet_by_name('Sheet1')
# 方法二: 通过表的索引来创建
# sheet = workbook.sheet_by_index(0) # 索引的下标是从0开头
# 操作表
# 1、查看表中的数据有多少行
print('总行数', sheet.nrows)
# 2、查看表中的数据有多少列
print('总列数', sheet.ncols)
# 3、查看某一行数据 索引是从0开始
print('行数据', sheet.row(1))  # 返回的是 数据类型:数据 以列表的形式返回
print('行的纯数据', sheet.row_values(1))  # 只返回数据
print('行数据的类型', sheet.row_types(1)) # 类型
# 4、查看某一列的数据
print('列的数据', sheet.col_values(2))
# 5、查看某一个单元格的数据
print(sheet.cell(0, 0))  # 返回数据类型和数据
print(sheet.cell_value(0,0))



