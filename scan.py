import socket
ip = str(input("Digite o ip: "))
ports = ""
def TENT(tipo):
    global ports
    if(tipo == 1):
        ports = [1,5,7,9,11,13,17,18,19,20,21,22,23,25,37,39,42,43,49,50,53,63,67,80,88,101,105,107,115,158,162,174,177,178,193,218,245,261,349,395,443,520,689,751,758,8080,9080]
        return(1)
    else:
        ports = range(10,99999)
        return(0)

tipo = TENT(int(input("Tipo: ")))
if(tipo == 1):
    pass
else:
    print("Loading ...")
for porta in ports:
    server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.settimeout(2)
    data = server.connect_ex((ip,porta))
    
    if(data == 0):
        print("[+] ]===> {} Porta Aberta".format(porta))
    if(data != 0 and tipo == 1):
        print("[!] ]---> {} Porta Fechada".format(porta))
    else:
        pass
        
server.close()
