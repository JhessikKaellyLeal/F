import socket
import sys
import os
import random
import time
try:
    ip = str(sys.argv[1])
except:
    print('Erro ...')
    time.sleep(4)
    os.system('exit')
    exit()
try:
    n = int(sys.argv[2])
except:
    n = 8080
try:
    t = int(sys.argv[3])
except:
    t = 1
color = ['2','a','3','8','9','c','e','f']
ports = range(0,n)
os.system('echo off')
os.system('title Scan')
os.system('cls')
os.system('color f')
print(']==> +++ [!] Iniciando o scan no ip: {} [!] +++\n'.format(ip))
time.sleep(4)
print('--> Portas abertas: \n')
for port in ports:
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(t)
    data = s.connect_ex((ip,port))
    if(data == 0):
        print(port)
    s.close()
    os.system('color {}'.format(str(random.choice(color))))

os.system('color f')