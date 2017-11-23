#!/usr/bin/python3
import socket

host = 'localhost'
port = 5000

s = socket.socket()
s.connect((host,port))

msg = s.recv(1024)

while msg:
   print('received: '+ msg.decode())
   msg = s.recv(1024)

s.close()
