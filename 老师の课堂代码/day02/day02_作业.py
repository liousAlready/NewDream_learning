'''
@File : day02_作业.py
@Time : 2021/3/31 20:03
@Author: luoman
'''
# import lib

# 列表进行反转
# sort(reverse=True) 排序
# reverse() 反转
list1 = [2, 4, 5, 7, 1]
print(list1[::-1])

# 切片 list
print(list1[0:])  # 从开头截取到末尾
print(list1[:])  # 表示整个列表
print('截取步长为2', list1[::2])  # 表示整个列表 :2 截取的步长
print('截取步长为-1', list1[::-1]) # 表示整个列表 :-1 从右往左进行截取

list2 = list1[:] # 把list1的所有数据复制给list2

