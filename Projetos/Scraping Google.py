from bs4 import BeautifulSoup as bs
import requests,time

pesquisa = str(input("[Digite a pesquisa:] }===> "))
url = "https://www.google.com/search?q={}".format(pesquisa)
pag = requests.get(url,headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})
pag = bs(pag.text,"html.parser")
conts = pag.find_all("div",{"class":"g"})
print("\n")
for c in conts:
    try:
        T = c.find("div",{"class":"ellip"}).text
        L = c.find("div",{"class":"TbwUpd"}).text
        print("[Google] ]=====> {}\n                 {}\n".format(T,L))
    except:
        pass
    
time.sleep(60)