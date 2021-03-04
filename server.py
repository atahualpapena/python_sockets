import socket

def Main():
    host = '192.168.1.153'
    port = 8004
    s = socket.socket()
    s.bind((host, port))
    print("server_running")
    s.listen(1)
    c, addr = s.accept()
    while True:
        data = c.recv(1024)
        if not data:
            break
        c.sendall(data)
        print(data)
    c.close()

Main()