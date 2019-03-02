class Person(object):
    def __init__(self,height,weight,age):
        self.height = height
        self.weight = weight
        self.age = age
    def getAge(self): # 属性用名词，方法用动词
        return self.age
    def eat(self):
        print("is eatting ")

