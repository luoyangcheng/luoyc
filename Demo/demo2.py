import socket
import threading

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',5555))
print(s.recv(1024))
data = input("请输入：")
s.send(data.encode())
print(s.recv(1024))

