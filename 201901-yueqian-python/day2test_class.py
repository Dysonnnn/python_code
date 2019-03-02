class ClassFbnx:
    # 初始化数据，__name__ 是系统函数
    def __init__(self,n1):  # self 是系统规定的，n1 是外部传进来的
        self.n = n1      # 外面传过来的值 n1 赋值  给 self
    def fbnxx(self):      # self 必须作为第一个参数
        value1 = 1
        value2 = 2
        for i in range(1,self.n+1):
            if i == 1  or i == 2:
                print("1")
            else:
                value = value1 + value2
                print(value)
                value1 = value2 # 向前移动一位
                value2 = value  # 向前移动一位

# 实例化
fbnx = ClassFbnx(20)
print(fbnx.n)  # 获取 n的值
print("/------------------------------/")
# 调用类的函数
fbnx.fbnxx()
print("/------------------------------/")