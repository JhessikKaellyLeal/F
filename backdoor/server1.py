import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("0.0.0.0",4567))
s.listen(1)
while True:
    obj,usu = s.accept()
    print("]=====> PC conectado {} ".format(usu))
    while True:
        msg = bytes(str(input("]====> Digite o comando: ")),"utf-8")
        obj.sendall(msg)
        msg = obj.recv(1024).decode("utf-8")
        print(msg)
