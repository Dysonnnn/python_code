from dya2pointDistance import *


# 测试用例
p1 = Distance(2,5,1,6)
p2 = Distance(1,8,10,3)        
od = p1.odistance(p2)
print("欧式距离\t = \t", od)

md = p1.mdistance(p2)
print("曼哈顿距离\t = \t", md)
