import socket
import select
# TCP 代理服务器
s = socket.socket()
s.bind(("127.0.0.1",8888))
s.listen(5)  # 5 最多可以


r_list=[s,]
while True:
    # 可读，可写，错误列表；  没信息过来就阻塞10s
    r1,w1,error = select.select(r_list,[],[],10) 
    for fd in r1:
        if fd == s: #第一次连接
            conn,addr = fd.accept() #产生新的连接对象，连接地址
            r_list.append(conn) #列表插入内容
            msg = conn.recv(200)  # 缓冲大小200字节
            conn.sendall("hello first".encode(encoding = 'GBK'))  #把信息发给所有用户
            
        else:
            msg = fd.recv(200)
            fd.sendall("hello again".encode(encoding = 'GBK'))  #把信息发给所有用户
s.close()