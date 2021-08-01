'''
@File : day01_5_列表.py
@Time : 2021/3/28 15:56
@Author: luoman
'''
# import lib
# 列表 list 使用频率比较高的一种数据类型
# 使用[] 进行定义，而且可以存储多个值，可以在一个列表中存多种数据类型  元素的个数是没有限制
# 定义列表
list1 = [1, 2, 3, 4, 5, 6]
list2 = [1, 1.2, 'python', [1, 2, 4]]
print(list1)
# 列表中可以嵌套列表
list3 = [[2, 3, 4]] # 定义了一个列表，列表只有一个元素[2, 3, 4]
list4 = [['x']]
# 列表与字符串有相似的操作：可以索引，切片，重复*，拼接+
# 索引：从左往右 下标从0开始  从右往左下标从-1开始
# 输出列表中的一个元素
print(list2[2])
print(list2[-1])
# 切片： 包头不包尾   变量名[起始值:结束值]
# 输出list1中2, 3, 4这几个值
print(list1[1:4])
# 要输出到结尾
print(list1[1:])
# 重复
print(list1 * 3)
# 拼接 +
print(list1 + list2)
# 假设要取出list4中的 'x'
print(list4[0])
print(list4[0][0])

# 列表也有处理函数
list5 = ['hello', 'python', '大太阳', '周末']
# 在列表的末尾追加元素 append(值)
list5.append('上班')
print(list5)
# print(list5.append('jj')) 错误操作
# 在指定位置插入元素:insert(位置,'值')
list5.insert(2, '放风筝')
print(list5)
# 告诉元素在什么位置 index('元素')
print(list5.index('大太阳'))
# 删除元素
list5.remove('上班')
print(list5)
# 统计某个元素出现的次数 count('元素')
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
print(list5.pop(1))  # 也可以删除指定位置的元素
print(list5)
# extend() 在列表上追加列表
list5.extend(list6)
print(list5)

# 列表给列表赋值 有两种情况
# 把list5 赋值给一个新的列表list8
list8 = list5  # 称之为取别名,对list5进行操作==对list8进行操作, 传地址
list5.append('打游戏')
print(list8)
# 打印某个变量的内存地址
print(id(list8))
print(id(list5))

# 把list5的值给list9
list9 = list5[:]  # 传值 克隆一个列表 1个列表变成2个
print(list9)
list5.append('熊孩子')
print(list5)
print(list9)
print(id(list9))
print(id(list5))

print('熊孩子' in list5)













