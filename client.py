import socket
import time

HOST = 'localhost'
PORT = 3000

S = socket.socket()
S.connect((HOST,PORT))

while True:
    data = S.recv(1024)
    print(data.decode('utf-8'))
    time.sleep(2)
    