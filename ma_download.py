from bs4 import BeautifulSoup as bs 
import os,socket,requests

url = "https://www.yumeost.com"
url1 = "https://www.yumeost.com/?s="

def cls():
    os.system("cls")

def pg2(ur):
    pg = bs(requests.get(str(ur)).text,"html.parser")
    cont = pg.find_all("div",{"class":"crownclowns"})
    cont2 = pg.find_all("div",{"class":"single-entry-wrap"})
    if(len(cont) != 0):
        try:
            ns = (cont[1]).find_all("ul")
            a = []
            num = 0
            print("")
            for n in ns:
                try:
                    name = (((str((n.find("h4")).text).split(':'))[1]).replace('“',"")).replace("”","")
                    a.append(((str(n.find("a"))).split('"'))[1])
                    print(f"\x1b[0;91m [{num}] \x1b[0;93m]---> \x1b[0;97m{name}\x1b[0;37m")
                    num = num + 1
                except:
                    pass

            numero = int(input("\n\x1b[0;97m Digite o numero do iten: \x1b[0;37m"))
            if(numero < len(a)):
                pass
            else:
                print("\n \x1b[0;91m[!] \x1b[0;93mnão tem esse iten \x1b[0;91m[!]\x1b[0;37m")

            pg2(a[numero])

        except:

            ns = (((cont[0]).find_all("tbody"))[0]).find_all("div")
            nst = (ns[1]).find_all("a")
            num = 0
            link = []
            print("")
            for n in nst:
                link.append((str(n).split('"'))[1])
                print(f"\x1b[0;91m [{num}] \x1b[0;93m]---> \x1b[0;97m{n.text}\x1b[0;37m")
                num = num + 1

            numero = int(input("\n\x1b[0;97m Digite o numero do iten: \x1b[0;37m"))
            if(numero < len(link)):
                pass
            else:
                print("\n \x1b[0;91m[!] \x1b[0;93mnão tem esse iten \x1b[0;91m[!]\x1b[0;37m")

            print(f"\n {link[numero]}")

    elif(len(cont2) != 0):
        ns = ((cont2[0]).find_all("tbody"))[0]
        nsf = ns.find_all("li")
        a = []
        num = 0
        print("")
        for n in nsf:
            name = (n.find("a")).text
            a.append((str(n.find("a")).split('"'))[1])
            print(f"\x1b[0;91m [{num}] \x1b[0;93m]---> \x1b[0;97m{name}\x1b[0;37m")
            num = num + 1
        numero = int(input("\n\x1b[0;97m Digite o numero da opição desejada: \x1b[0;37m"))
        if(numero < len(a)):
            pass
        else:
            print("\n \x1b[0;91m[!] \x1b[0;93mnão tem essa opição \x1b[0;91m[!]\x1b[0;37m")
            exit()
        print(f"\n {a[numero]}")    


    else:
        pass

def pg1():
    nome = str(input("\x1b[0;97m Digite o nome do anime: \x1b[0;37m"))
    pgs = bs(requests.get(f"{url1+nome}").text,"html.parser")
    cont = pgs.find_all("div",{"class":"post-outer col-sm-3 col-xs-6"})
    cont1 = (pgs.find_all("div",{"class":"pagination-num"}))[0]
    n = cont1.find_all("a")
    a = []
    for al in n:
        a.append((str(al).split('"'))[3])

    for pgst in range(0,len(a)):
        pgs = bs(requests.get(a[pgst]).text,"html.parser")
        cont0 = pgs.find_all("div",{"class":"post-outer col-sm-3 col-xs-6"})
        cont = cont + cont0

    l = []
    num = 0
    for c in cont:
        name = c.text
        l.append((str((c.find_all("a",{"class":"post-title-link"})[0])).split('"'))[3])
        print(f"\x1b[0;91m [{num}] \x1b[0;93m]---> \x1b[0;97m{name}\x1b[0;37m")
        num = num + 1
        try:
            l.remove("bookmark")
        except:
            pass
    numero = int(input("\n\x1b[0;97m Numero do iten: \x1b[0;37m"))
    if(numero < len(l)):
        pass
    else:
        print("\n \x1b[0;91m[!] \x1b[0;93mnão tem essa opição \x1b[0;91m[!]\x1b[0;37m")
        exit()
    
    pg2(l[numero])
        
def inr():
    pg = bs(requests.get(url).text,"html.parser")
    cont = (pg.find_all("div",{"class":"blog-content-inner"}))[0]
    cont2 = cont.find_all("h2",{"class":"post-title entry-title is-size-4"})
    print("\x1b[0;93m Ultimos adicionados:\n\x1b[0;37m")
    for c in cont2:
        name = c.text
        print(f"\x1b[0;93m Anime \x1b[0;91m- \x1b[0;96mMusicas: \x1b[0;97m{name}\x1b[0;37m")
    print("")
    pg1()

cls()
inr()