# 根据如图所示，类之间的关系，写出对应的代码

class 妖(object):
    def __init__(self,name):
        self.name = name
    def getName(self):
        print(" name : ",self.name)

class 蛇妖(妖):
    pass

class 白蛇(蛇妖):
    pass

class 青蛇(蛇妖):
    pass    

class 人:
    def __init__(self,name):
        self.name = name
    def getName(self):
        print(" name : ",self.name)
    def catch(self,yao):
        if isinstance(yao,妖): #判断是不是妖
            print(self.name + " 抓妖： " + yao.name)
        else:
            print(self.name + " 无法实现抓 " + yao.name)
    def like(self,yao):
        if isinstance(yao,白蛇): #判断是不是白蛇
            print(self.name + " 喜欢妖： " + yao.name)
        else:
            print(self.name + " 不喜欢 " + yao.name)

xuxian =  人("许仙")  
fahai = 人("法海")         
bsz = 白蛇("白素贞")
xq = 青蛇("小青")

xuxian.catch(fahai)
xuxian.like(fahai)
xuxian.like(bsz)
fahai.catch(xuxian)
fahai.catch(xq)