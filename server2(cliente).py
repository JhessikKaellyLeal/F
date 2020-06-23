import socket
ip = '192.168.42.211'
port = 4567
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.connect((ip,port))
print (server.recv(1024))
