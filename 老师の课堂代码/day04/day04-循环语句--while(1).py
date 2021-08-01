'''
@File : 循环语句--while.py
@Time : 2021/4/11 09:36
@Author: luoman
'''
# import lib
'''
while 判断条件： 
          执行语句…… 
[else： 
          执行语句……]
'''
# 举例：要求输出一个故事五次：故事的内容是：这是一个悲伤的故事
print('这是一个悲伤的故事')
print('这是一个悲伤的故事')
print('这是一个悲伤的故事')
print('这是一个悲伤的故事')
print('这是一个悲伤的故事')
# 循环要进行使用的四个基本条件：1、起始值  2、结束值  3、循环体  4、增量(步长)
# 某个操作如果要重复执行，使用循环
init = 1  # 起始值
while init <= 5:  # 是否继续循环的判断(结束条件)
    print('这是一个悲伤的故事')
    init = init + 1
else:
    print('故事讲完了')

# 举例：计算1--100之间的和
sum = 0  # 求的和
i = 1
while i <= 100:
    sum = sum + i
    i = i+1
else:
    print(sum)
'''
+:二元运算符  1+2
sum=0
0+1=1
    1+2=3
        3+3=6
            6+4=10
                10+5=15
                     sum+ i = sum 
'''
'''
while 与 if 嵌套
'''
# 算出1--10之间的偶数和
i = 1
sum = 0
while i <= 10: # 2  4   6  8  10
    if i % 2 == 0:
        sum = sum + i

    i = i + 1
else:
    print(sum)

# while循环的嵌套
'''

while 判断条件： 
       
    while 判断条件： 
          执行语句…… 
    [else： 
          执行语句……]

[else： 
          执行语句……]
'''
# 需求1: 要求输出一行 一个*
print('*')
# 需求2: 要求输出一行 五个*
print('===========需求2=========')
print('*', end='\t')
print('*', end='\t')
print('*', end='\t')
print('*', end='\t')
print('*', end='\t')
print()

# 改良成while语句
print('===========改进成while循环=========')
n = 1
while n <= 5:
    print('*', end='\t')

    n = n+1
print()

# 需求3: 要求输出五行 五个*：把一行五个*的需求重复做5次
print('===========需求3=========')
n = 1
while n <= 5:
    print('*', end='\t')

    n = n+1
print()

n = 1
while n <= 5:
    print('*', end='\t')

    n = n+1
print()

n = 1
while n <= 5:
    print('*', end='\t')

    n = n+1
print()

n = 1
while n <= 5:
    print('*', end='\t')

    n = n+1
print()

n = 1  # 一行 的几个
while n <= 5:
    print('*', end='\t')

    n = n+1
print()

print('=========继续改进行while循环==========')
k = 1  # k 表示行数
while k <= 5:
    # 循环体--重复的操作
    n = 1  # 一行 的几个
    while n <= 5:
        print('*', end='\t')

        n = n + 1
    print()

    k=k+1
#  九九乘法表
''''
1 * 1 =1
1 * 2 =2   2 * 2=4
1 * 3 =3   2 * 3=6 3*3=9
'''

print('=========九九乘法表========')
i = 1
j = 1
print('%d * %d = %d' % (i, j, i*j), end='\t')
j=j+1
print('%d * %d = %d' % (i, j, i*j), end='\t')
j=j+1
print('%d * %d = %d' % (i, j, i*j), end='\t')
j=j+1
print('%d * %d = %d' % (i, j, i*j), end='\t')
j=j+1
print('%d * %d = %d' % (i, j, i*j), end='\t')
j=j+1
print('%d * %d = %d' % (i, j, i*j), end='\t')
j=j+1
print('%d * %d = %d' % (i, j, i*j), end='\t')
j=j+1
print('%d * %d = %d' % (i, j, i*j), end='\t')
j=j+1
print('%d * %d = %d' % (i, j, i*j), end='\t')
print()
# 改进while循环
print('===========改进成while循环=========')
i = 1
j = 1
while j<=9:
    print('%d * %d = %d' % (i, j, i * j), end='\t')
    j = j + 1

print()
# 改进成9个行
j = 1
while j<=9:
    print('%d * %d = %d' % (i, j, i * j), end='\t')
    j = j + 1
print()

j = 1
while j<=9:
    print('%d * %d = %d' % (i, j, i * j), end='\t')
    j = j + 1
print()

j = 1
while j<=9:
    print('%d * %d = %d' % (i, j, i * j), end='\t')
    j = j + 1
print()

print('=========继续改进行while嵌套循环==========')
i = 1
while i<=9:
    j = 1
    while j <= i:
        print('%d * %d = %d' % (j, i, i * j), end='\t')
        j = j + 1
    print()

    i = i+1

# 有时候需要故意成死循环---> 无条件开始循环
# while True:
# 给一个结束的条件：一般是结合if语句：break continue











