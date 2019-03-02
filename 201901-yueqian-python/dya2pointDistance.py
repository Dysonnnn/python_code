'''
计算距离，一个点四个坐标
面向对象编程
P1(2,5,1,6)
P2(1,8,10,3)

计算欧式距离和曼哈顿距离，两个距离越相近，就越相似

'''
# 类 距离
class Distance:
    def __init__(self,x1,x2,x3,x4):
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
    def odistance(self,p2):  # p2指的是Distance 另一个点
        # 点与点之间距离公式   return 返回值
        return ((self.x1 - p2.x1)**2 + (self.x2 - p2.x2)**2 + (self.x3 - p2.x3)**2 + (self.x4 - p2.x4)**2)**0.5   

    def mdistance(self,p2):
         # 点与点之间的曼哈顿距离公式   return 返回值
        return abs(self.x1 - p2.x1)+abs(self.x2 - p2.x2)+abs(self.x3 - p2.x3)+abs(self.x4 - p2.x4)


'''
# 测试用例
p1 = Distance(2,5,1,6)
p2 = Distance(1,8,10,3)        
od = p1.odistance(p2)
print("欧式距离\t = \t", od)

md = p1.mdistance(p2)
print("曼哈顿距离\t = \t", md)
'''