# 导入 文件 ** 中的 所有内容
from day2classPerson import *

class Student(Person):
    def __init__(self,height,weight,age,name):
        # 复写代码
        super(Student,self).__init__(height,weight,age)
        self.name = name
    def eat(self):
        print(self.name + " is eating") # 多态性 ,继承之后重写函数

zhangsan = Student(170,60,20,"zhangsan")
print(zhangsan.getAge())
zhangsan.eat()

'''
class Student(object):
    def __init__(self,height,weight,age,name):
        self.height = height
        self.weight = weight
        self.age = age
        self.name = name
    def getAge(self): # 属性用名词，方法用动词
        return self.age
    def eatlunch(self):
        print(self.name + " is eatting ")
    def getName(self):
        return self.name
'''