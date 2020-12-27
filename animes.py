from bs4 import BeautifulSoup as bs
import requests,time,os

def cls():
    os.system("cls")

def req():
    pg = bs(requests.get("https://goyabu.com/").text,"html.parser")
    cont = (pg.find_all("div",{"class":"loop-content phpvibe-video-list miau"}))[0]
    cont2 = cont.find_all("div",{"class":"video"})
    cls()
    print("")
    for c in cont2:
        name = str(c.find("h4").text)
        t = (str((c.find_all("li"))[2]).replace("<li>","")).replace("</li>","")
        print(f"\x1b[0;94m Anime: \x1b[1;93m{name} \x1b[1;91m-<>- \x1b[1;96m{t}\x1b[0;37m")

while True:
    req()
    time.sleep(60)