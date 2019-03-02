'''
斐波那契数列 后一个数字是前两个数字的 和
1 把斐波那契数列的前20个元素写入一个list列表中
1 1 2 3 5 8 13 21 ……
'''

'''
# 最简单的方法
# 定义第一、二个的值
value1 = 1
value2 = 2
for i in range(21):
    if i == 1  or i == 2:
        print("1")
    else:
        value = value1 + value2
        print(value)
        value1 = value2 # 向前移动一位
        value2 = value  # 向前移动一位

'''

# 定义函数
def fbnx(n = 2):  # 设置缺省值
    value1 = 1
    value2 = 2
    for i in range(1,n+1):
        if i == 1  or i == 2:
            print("1")
        else:
            value = value1 + value2
            print(value)
            value1 = value2 # 向前移动一位
            value2 = value  # 向前移动一位

a = fbnx  # 地址赋值给a，a的效果也一样
fbnx(20)

print("输出缺省值")
fbnx()

