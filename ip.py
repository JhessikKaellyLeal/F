import socket
import time
ips = ["192.168.1.1","192.168.0.1","192.168.1.10","192.168.0.10","192.168.1.100","192.168.0.100","10.0.0.1","10.0.0.10","10.0.0.100"]
ports = [21,80,443,8080]
for ip in ips:
    for port in ports:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        c = s.connect_ex((ip,port))
        if(c == 0):
            print("IP =====> {} Port =====> {}".format(ip,port))
        else:
            pass