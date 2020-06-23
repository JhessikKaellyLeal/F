import os
import sys
import time
import socket

if("-r" in sys.argv):
        ip = sys.argv[int(sys.argv.index("-r"))+1]
        n = os.system("tracert "+ip)
        print(n)

if("-s" in sys.argv):
    ip = sys.argv[int(sys.argv.index("-s"))+1]
    if("-p" in sys.argv):
        port1 = int(sys.argv[int(sys.argv.index("-p"))+1])
        port2 = int(sys.argv[int(sys.argv.index("-p"))+2])
        l = range(port1,port2)
    else:
        l = range(0,8080)
    for c in l:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(1)
        re = s.connect_ex((ip,c))
        if(re == 0):
            print("[Porta Aberta] ]===> {}:{}".format(ip,c))
        else:
            print("]==> Porta Fechada {}".format(c))

