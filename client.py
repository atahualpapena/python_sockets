import socket

def Main():
    host = '192.168.1.153'
    port = 8004 
    s = socket.socket()
    s.connect((host,port))
    message = input("->")
    while message != 'q':
        s.send(message.encode('utf-8'))
        data = s.recv(1024)
        message = input("->")
    s.close()

Main()