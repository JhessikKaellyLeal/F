from bs4 import BeautifulSoup as bs
import requests,os

url = "https://animestorrent.com/?s="
url2 = "https://animestorrent.com/category/lancamento/"

def r(link):
    return bs(requests.get(link).text,"html.parser")

def cls1():
    os.system("cls")

def dow(url):
    pg = r(url)
    cont = (pg.find_all("ul",{"class":"buttons"}))[0]
    link = cont.find("li")
    cont2 = str(link).split("<li>")
    link2 = cont.find_all("a")

    n = 0
    l = []
    print("")
    for c in cont2:
        if(("720p" in (str(c))) or ("1080p" in (str(c)))):
            ty = (c.split('<a href="'))[0]
            if(ty == ""):
                ty = ((((c.split("<span>"))[1]).replace("</span>","")).replace("</a>","")).replace("</li>","")
                if(ty == ""):
                    pass
                else:
                    l.append((c.split('"'))[1])
                    print(f"\x1b[0;91m [{n}] \x1b[0;96m{ty}\x1b[0;37m")
                    n = n + 1
            else:
                l.append((c.split('"'))[1])
                print(f"\x1b[0;91m [{n}] \x1b[0;96m{ty}\x1b[0;37m")
                n = n + 1
        else:
            pass
    if(len(l) == 0):
        n = 0
        for c in link2:
            ty = str((c.find("span")).text).replace(":","")
            l.append((str(c).split('"'))[1])
            print(f"\x1b[0;91m [{n}] \x1b[0;96m{ty}\x1b[0;37m")
            n = n + 1
    else:
        pass
    
    if(len(l) == 0):
        print(" \x1b[0;91m[!] \x1b[0;97mAnime não disponivel para download \x1b[0;91m[!]\x1b[0;37m")
        exit()
    else:
        pass
    print("")
    num = int(input("\x1b[0;97m Digite o numero da resolução a baixar: \x1b[0;37m"))
    if(num < len(l)):
        pass
    else:
        print("\n\x1b[0;97m Não possui essa opição\x1b[0;37m")
        exit()
    
    print(f"\n {l[num]}\x1b[0;37m")
    exit()
    
def pg1():
    pg = r(url2)
    c = (pg.find_all("div",{"class":"movies-list"}))[0]
    c2 = c.find_all("div",{"class":"title"})
    c3 = c.find_all("span",{"class":"imdb"})
    n = 0
    print("\n \x1b[0;93mUltimos lançamentos\n")
    for t in c2:
        print(f"\x1b[0;97m Anime: \x1b[1;96m{t.text} \x1b[0;97m{(str((c3[n]).text).split())[0]} \x1b[1;91m{(str((c3[n]).text).split())[1]}\x1b[0;37m")
        n = n + 1

def pg2():
    name = str(input("\n \x1b[0;97mNome do anime a ser pesquisado: \x1b[0;37m"))
    pg = r(f"{url+name}")
    c = (pg.find_all("div",{"class":"movies-list"}))[0]
    c2 = c.find_all("div",{"class":"title"})
    if(len(c2) < 1):
        print("\n\x1b[0;97m Não encontrado\n\x1b[0;37m")
        exit()
    else:
        pass
    c3 = c.find_all("span",{"class":"imdb"})
    c4 = c.find_all("div",{"class":"image"})
    n = 0
    l = []
    print("")
    for t in c2:
        try:
            print(f"\x1b[0;92m [{n}]\x1b[0;97m Anime: \x1b[1;96m{t.text} \x1b[0;97m{(str((c3[n]).text).split())[0]} \x1b[1;91m{(str((c3[n]).text).split())[1]}\x1b[0;37m")
            c5 = (c4[n].find_all("a"))
            l.append((str(c5).split('"'))[1])
            n = n + 1
        except:
            pass
    try:
        num = int(input("\n\x1b[0;97m Digite o numero referente ao anime que você quer baixar: \x1b[0;37m"))
        if(num < (len(l))):
            pass
        else:
            exit()
    except:
        print("\x1b[0;97m Deveria ter digitado o numero referente ao anime\x1b[0;37m")
        exit()
    
    dow(str(l[num]))

cls1()
pg1()
pg2()