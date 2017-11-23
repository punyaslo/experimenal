#!/usr/bin/python3
import socket

host = 'localhost'
port = 5000

s = socket.socket()

s.bind((host,port))

s.listen(2)

c,addr = s.accept()
print("Connection from:", str(addr))

c.send(b'hello client\n')
msg = 'greeting from the server'

c.send(msg.encode())

c.close()
