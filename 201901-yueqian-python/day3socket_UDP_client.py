# -*-coding:utf-8 -*-
import socket

# 创建一个数据报套接字 用于UDP传输
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
'''
socket.AF_INET表示IPV4     socket.AF_INET6表示IPV6
SOCK_STREAM：流式套接字。主要用于TCP协议
SOCK_DGRAM：数据报套接字。主要用于UDP协议
'''
print("socket 创建成功 \n",sock)
sock.bind(('',9527))  #监听端口

content,srcinfo = sock.recvfrom(1024)  #接收1024字节数据
print(content.decode("GBK"))   # 字节码 解码

sock.close()   # 关闭链接  节省资源