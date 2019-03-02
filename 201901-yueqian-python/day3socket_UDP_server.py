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


sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1) # 1 允许广播
dest = ('<broadcast>',8080)  # 元组，监听8080 端口

sock.sendto("hello哈哈哈".encode(encoding="GBK"),dest)  # sendto是UDP的发送命令   发送的信息，编码（中文的话要设置为utf-8），地址




sock.close()   # 关闭链接  节省资源