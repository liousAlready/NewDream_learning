'''

while 判断条件:
    执行语句...
[else:
    执行语句...]


'''

# 　举例：要求输出一个故事五次：故事的内容是：这是一个悲伤的故事
# print("人类的悲伤并不相通")
# print("人类的悲伤并不相通")  重复五遍效率低下
# print("人类的悲伤并不相通")
# print("人类的悲伤并不相通")
# print("人类的悲伤并不相通")

# 循环要进行使用的四个基本条件: 1.起始值 2.结束值 3.循环体 4.增量(步长)
# 某个操作如果要重复执行,使用循环
init = 0
while init <= 5:
    init = init + 1
    print("跟你讲个故事:人类的悲伤并不相通")
else:
    print("故事讲完了")

# 举例: 计算1--100的和
sum = 0
i = 1
while i <= 100:
    sum = sum + i
    i = i + 1
else:
    print(sum)

'''
+: 二元运算符 1+2
sum = 0 
0+1 = 1
    1+2 =3
        3+3 = 6
            6+4 = 10
                sum = sum + i     
'''

'''
while 与 if 嵌套

'''
# 计算1--10之间的偶数和
i = 1
sum = 0
while i <= 10:  # 2 4 6 8 10 = 30
    if i % 2 == 0:
        sum = sum + i
    i = i + 1
else:
    print(sum)

# while循环嵌套
'''
while 判断条件：
    while 判断条件：
        执行语句...
    [else:
        执行语句...]
[else:
        执行语句...]
'''

# 需求1：要求输出一行 一个*
print("*")

# 需求2：要求输出一行 五个*
print("=====需求2=====")
print("*", end="\t")
print("*", end="\t")
print("*", end="\t")
print("*", end="\t")
print("*", end="\t")
print()

# 改良需求2：
print("=====改进成while循环=====")
n = 1
while n <= 5:
    print("*", end="\t")

    n = n + 1
print()

# 需求3：要求输入五行 五个*:把一行五个*的需求重复做5次
n = 1
while n <= 5:
    print("*", end="\t")

    n = n + 1
print()
n = 1
while n <= 5:
    print("*", end="\t")

    n = n + 1
print()
n = 1
while n <= 5:
    print("*", end="\t")

    n = n + 1
print()
n = 1
while n <= 5:
    print("*", end="\t")

    n = n + 1
print()
n = 1
while n <= 5:
    print("*", end="\t")

    n = n + 1
print()

print("======继续改进while循环========")
k = 1  # 表示行数
while k <= 5:
    # 循环体--重复的操作
    n = 1  # 一行的个数
    while n <= 5:
        print("*", end="\t")

        n = n + 1
    print()

    k = k + 1

# 九九乘法表
'''
1*1 =1
1*2 =2 2*2=4
1*3 =3 2*3=6 3*3=9
'''
print("======99乘法表========")
i = 1  # 表示行数
j = 1  # 1

while j <= 9:
    print("%d * %d = %d" % (i, j, i * j))
    j = j + 1

print("======99乘法表继续改进========")
i = 1
while i <= 9:
    j = 1
    while j <= i:
        print("%d * %d = %d" % (j, i, i * j), end='\t')
        j = j + 1
    print()

    i = i + 1

# 有时候需要故意造成死循环 -->无条件开始循环
# while True:  #无条件进行循环
# 给一个结束的条件： 一般结合if语句：break continue



