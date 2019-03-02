import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.bind(('',9527))
msg = '1:1234567:陌生人:不知道谁的的电脑:32:你今晚在家吗?'
sock.sendto(msg.encode(encoding = 'gbk'),("192.168.211.1",2425))
sock.close()