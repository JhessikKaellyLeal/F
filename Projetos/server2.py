import socket
ip = '0.0.0.0'
port = 4567
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))
server.listen(5)
(obj,cliente) = server.accept()
print ('Maquina conectada: ',cliente)
obj.send("ola")
server.close()
