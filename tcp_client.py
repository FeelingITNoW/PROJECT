import socket

clientsocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(("54.179.155.51", 58913))
clientsocket.send('ZIMZALABIM'.encode())
