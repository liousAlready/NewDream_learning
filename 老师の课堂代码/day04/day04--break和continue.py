'''
@File : day04--break和continue.py
@Time : 2021/4/11 11:08
@Author: luoman
'''
# import lib
# break 和 continue
# break:破坏，跳出本层循环
# continue: 继续，结束本次循环，继续下一次循环
i = 1
while i <= 10:
   i = i + 1
   if i == 5:
       break

   print(i, end='\t')

print('结束')

i = 1
while i <= 10:
   i = i + 1
   if i == 5:
       continue
   print(i, end='\t')
else:
 print('结束')
print('============当j=5的时候 break========')
i = 1
while i <= 9:
    j = 1
    while j <= i:
        if j == 5:
            break
        print('%d * %d = %d' % (j, i, i * j), end='\t')
        j = j + 1
    print()

    i = i + 1

n = 1
while True:
    print(n)
    n = n +1
    if n == 4:
        break

# 举例：如果用户输入0 表示程序结束，如果输入1表示：登陆，输入2 = 注册，输入3：查询
while True:
    start = int(input('请输入你要进行的操作:'))
    if start == 0:
         print('程序结束')
         break
    elif start ==1:
        print('登陆')
    elif start == 2:
        print('注册')
    elif start ==3:
        print('查询')
    else:
        print('输入有误')
