import socket,sys

if(len(sys.argv) > 2):
    if("-i" in sys.argv):
        ip = str(sys.argv[int(sys.argv.index("-i"))+1])
    else:
        ip = "0.0.0.0"
    if("-p" in sys.argv):
        try:
            portin = int(sys.argv[int(sys.argv.index("-p"))+1])
            portout = int(sys.argv[int(sys.argv.index("-p"))+2])
            ports = range(portin,portout)
        except:
            print("]=====> ERRO!\n]======> Tem que colocar a porta inicial e a final\nExemplo:\n   py scan.py -i [ip] -p [p1] [p2]")
            exit()
    else:
        ports = range(0,8080)
    for port in ports:
        s1 = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s1.settimeout(3)
        s2 = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s2.settimeout(3)
        TCP = s1.connect_ex((ip,port))
        UDP = s2.connect((ip,port))
        if(TCP == 0):
            print("]====> Porta {} TCP aberta no IP {}".format(port,ip))
        if(UDP == 0):
            print("]====> Porta {} UDP aberta no IP {}".format(port,ip))

else:
    print("]====> ERRO!\n]====> Tem que colocar -i e o ip na frente\nExemplo: \n   py scan.py -i [ip]")
    exit()