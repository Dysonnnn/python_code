import paho.mqtt.client as mqtt
import json

def on_connect(client,userdata,flag,rc): # 名称没有限定
    #rc 是连接结果
    print("connect result code " + str(rc))
    client.subscribe("chat") # 订阅主题 chat
    #往主题 chat 发送消息 
    client.publish("chat",json.dumps({"user":user,"say":" hello,anyone"}))
    # json.dumps() 填写的内容是字典  将对象转换为串 序列化

def on_message(client,userdata,msg): #名称自定义的
    #json.loads()  反序列化函数
    payload = json.loads(msg.payload.decode()) #msg 中有 主题信息 和 字符串消息
    print(payload.get("user")+" say :"+payload.get("say"))

# 主项目的运行入口点,第三方执行代码的时候不能执行本文件
# 避免第三方文件 import 本文件
if __name__ == "__main__":
    client = mqtt.Client()
    client.username_pw_set("admin","password") #设置mqtt的账号密码
    HOST = "127.0.0.1"
    client.on_connect = on_connect #传输地址，事件产生的话自动调用
    client.on_message = on_message # 有消息来救触发

    # 绑定服务器
    client.connect(HOST,1883,60) #服务器地址 端口号 60s判断一次连接是否存在
    user = input("please input  username: ")
    client.user_data_set(user) #设置连接的用户
    client.loop_start() #一直通信

    while True: 
        str = input()
        if str:
            client.publish("chat",json.dumps({"user":user,"say":str}))
        else:
            print("--------------Exit--------------")

