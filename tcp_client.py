#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

# # AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect(('www.sina.com.cn', 80))
# s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

# # 接收数据
# buffer = []
# while True:
# 	# 每次最多接收1k字节
# 	d = s.recv(1024)
# 	if d:
# 		buffer.append(d)
# 	else:
# 		break
# data = b''.join(buffer)

# # 关闭连接
# s.close()

# header, html = data.split(b'\r\n\r\n', 1)
# print(header.decode('utf-8'))

# # 把接收的数据写入文件
# with open('sina.html', 'wb') as f:
# 	f.write(html)

######################### 客户端 #########################

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
print(s.recv(1024).decode('utf-8')) # 接收欢迎消息

for data in [b'Michael', b'Tracy', b'Sarah']:
 	s.send(data)
 	print(s.recv(1024).decode('utf-8'))

s.send(b'exit')
s.close()