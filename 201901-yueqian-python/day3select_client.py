import socket
import select
# TCP客户端
s = socket.socket()
s.connect(("127.0.0.1",8888)) #连接服务器 地址

flag = 1
while flag:
    input_msg = input("please input >>> ") # 提示内容，输入内容
    if input_msg == "0":
        break
    s.sendall(input_msg.encode())  # encode() 缺省值是识别英文的
    msg = s.recv(1024)  # 接收1024字节信息
    print(msg.decode())  # 打印解码后的信息

        

s.close()        