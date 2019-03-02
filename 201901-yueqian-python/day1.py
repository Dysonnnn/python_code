str_test2 = "hi"
int_test2 = 5

test2 = "hello world %s ---- %d"%(str_test2,int_test2)

print('\n')

print(test2)

print('ahahahhaha')

dec = 17
print(dec)
print(bin(dec)) # 转换为二进制
print(oct(dec)) # 转换为八进制
print(hex(dec)) # 转换为十六进制

print(3/2)  # python3 的结果 是 1.5   javascrip是 1.5
print(3//2) # 整除 
print(7%2)  # 取模  取余数
print(2**10) # 求幂
print(0**0) # 求幂  0^0 = 1


test4 = 15
test44 = "15"
print(test4==test44)  #False



str_test4 = "hello"
print('e' in str_test4)  #判断字符是否在是否在字符串中


print(id(test4))   # id() 返回变量地址
print(id(test44))

# 不可变数据类型，同样的值，具有相同的地址，不会有重复，节约内存地址



# 多分支条件判断
score = 87
if score>=90:
    print("优秀")
elif score>=80 and score <90:    
    print("良好")
elif score>=60 and score <80:    
    print("中等")
else:
    print("不及格")    

count = 1
mu = 1
while count <=100:
	mu = mu * count
	count = count +1

print("结果是：",mu)	





print("/----------over----------/")