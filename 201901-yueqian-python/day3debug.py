'''
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
dest=('<broadcast>',8080)
s.sendto('hello'.encode(),dest)
print(s)
s.close()

'''

'''
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
dest=('<broadcast>',8080)
s.sendto('hello'.encode(encoding="gbk"),dest)
print(s)
s.close()


print("jah哈哈哈")


'''


import pymysql  # python mysql 
# MySQLHOST = "localhost"
MySQLHOST = "47.106.251.208"
MySQLUser = "mqttuser"
MySQLPassWord = "mqttmqtt"
MySQLDataBase = "mqtt"
MQTTHOST = "47.106.251.208"
#MQTTHOST = "127.0.0.1"
MQTTPORT = 1883

recv = '37,56'
temp = str(recv[0:2]) + str("°C")  #温度 
hum =  str(recv[3:5]) + str("%")   #湿度
print (temp,hum)

# 连接数据库
db = pymysql.connect(MySQLHOST,MySQLUser,MySQLPassWord,MySQLDataBase)
# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()      

sql_insert="insert into temphumdata values(%s,%s,%s)"


try:
    cursor.execute(sql_insert, (temp,temp,hum))
except:
    # 如果发送错误则回滚
    print("/-------mysql  insert error! ----------------/")
    db.rollback()    