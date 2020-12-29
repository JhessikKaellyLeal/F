import os
import socket
host = str(input("Digite a url(sem http:// https://): "))
exe = str(os.popen("ping "+host).read())
print(exe)
exe = exe.split("[")
exe = exe[1].split("]")
ip = exe[0]
exe2 = os.popen("tracert "+host).read()
print(exe2)
port = range(20,8080)
for t in port:
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.settimeout(0.2)
    data = server.connect_ex((ip,t))
    if(data == 0):
        print("[+] ]===> {} Porta Aberta".format(t))
    else:
        pass
