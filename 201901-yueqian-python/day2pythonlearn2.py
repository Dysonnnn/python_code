a = 3
b =5
#交换数据：
##方法一：
temp = 0	
temp = b
b = a
a = temp
print(a,b)
##方法二：
a,b = b,a
print(a,b)

print("/------------------------------/")


zhangsan  = {"name" : "zhangsan","age" : 20}

print(zhangsan.get("age"))  #获取字典的值
#集合、字典遍历
for key,value in zhangsan.items():
	print(key,value)

print("/------------------------------/")

list1 = [2,3,"true","hello"]
print(len(list1))
# 列表遍历方式
for i in list1:
	print(i)



