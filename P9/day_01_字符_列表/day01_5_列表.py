#!/usr/bin/env python
# encoding: utf-8
'''
@contact: 1650503480@qq.com
@file: day01_5_列表.py
@time: 2021/3/28 16:10
'''

# 列表list 使用频率比较高

list1 = [1, 23, 4, 5, 1, 5, 1]
list2 = [11]
list3 = [11]
list4 = [11, 5, 15, 5, 1, 25, 21, 56, 16]
# 切片： 包头不包尾  变量名 [起始值：结束值]
# 输出 list1中2，3，4这几个值
print(list1[1:4])
# 要输出到结尾
print(list1[1:])
# 重复
print(list1 * 3)
# 拼接 +
print(list1 + list2)
# 假设要去除list4中的'x'
print(list4[0])
# print(list4[0][0])

# 列表也有处理函数
list5 = ['hello', 'python', '大太阳', '周末', '上班']
# 在列表的末尾追加原酸 append(元素)
print(list5)
# print(list5.append('jj'))

# 在指定位置插入元素：insert(位置，'值')
list5.insert(2, '放风筝')
print(list5)
# 告诉指定位置的元素在什么 index('元素')
print(list5.index('大太阳'))

# 删除列表中的元素
list5.remove('上班')
print(list5)
# 统计某个元素出现的次数，count('元素')
print(list5.count('周末'))

# 排序 sort() 升序和降序
list6 = [2, 6, 3, 5, 0]
list6.sort()  # 默认升序
print(list6)

# 降序
list6.sort(reverse=True)  # reverse 反转
print(list6)

# 反转 reverse() 只进行反转，不排序
list7 = [2, 6, 3, 5, 0]
list7.reverse()
print(list7)

# pop() 删除列表最末尾的元素，并返回该元素
print(list5.pop())
print(list5.pop(1))  # 删除指定位置的元素
print(list5)

# extend() 在列表上追加列表
list5.extend(list6)
print(list5)

# 列表给列表赋值 有两种情况
# 把list5赋值给新的列表 list8
list8 = list5  # 取别名,对list5进行操作==对list8进行操作，传地址
list5.append('打游戏')
print(list8)

# 打印某个变量的内存地址
print(id(list8))
print(id(list7))

# 把list5的值给list9
list9 = list5[:] # 传值 克隆一个列表 1个列表变成2个
print(list9)
list5.append('熊孩子')
print(list5)
print(list9)

list10=["hello",'python','太阳','周末']
print(list10)