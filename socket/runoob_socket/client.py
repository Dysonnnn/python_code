# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket               # 导入 socket 模块

s = socket.socket()         # 创建 socket 对象
host = socket.gethostname() # 获取本地主机名
#host = ''
port = 1234                # 设置端口好

s.connect((host, port))
print s.recv(1024)
#s.send()
s.close()
