from tkinter import *
from bs4 import BeautifulSoup as bs
import requests

header ={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.104 Safari/537.36"}

def inic():
    global nomes,links,li,t1,b2
    li.destroy()
    t1.destroy()
    b2.destroy()
    url = "https://animestorrent.com/"
    pag = bs(requests.get(url,headers=header).text,"html.parser")
    cont = pag.find_all("article",{"class":"bs styletere"})
    nomes = []
    links = []
    for c in cont:
        nome = str(c.find("h2").text)
        a = (str((c.find("div")).find("a")).split('"'))[3]
        nomes.append(nome)
        links.append(a)
    
    t1 = Label(tela,text="Ultimos Adicionados:",font="Arial 12 bold")
    t1.place(x=1,y=50)
    li = Listbox(tela,width=40,height=20)
    li.place(x=5,y=80)
    b2 = Button(tela,text="Ver",font="Arial 12 bold",bg="#098",fg="#fff",width=8,command=download)
    b2.place(x=300,y=200)
    for no in nomes:
        li.insert(END,no)

def inic2(url):
    global nomes,links,li,t1,b2
    li.destroy()
    t1.destroy()
    b2.destroy()
    pag = bs(requests.get(url,headers=header).text,"html.parser")
    cont = pag.find_all("div",{"class":"excstf"})
    cont = pag.find_all("article",{"class":"bs"})
    nomes = []
    links = []
    for c in cont:
        nome = str(c.find("h2").text)
        a = (str((c.find("div")).find("a")).split('"'))[3]
        nomes.append(nome)
        links.append(a)
    
    t1 = Label(tela,text="Ultimos Adicionados:",font="Arial 12 bold")
    t1.place(x=1,y=50)
    li = Listbox(tela,width=40,height=20)
    li.place(x=5,y=80)
    b2 = Button(tela,text="Ver",font="Arial 12 bold",bg="#098",fg="#fff",width=8,command=download)
    b2.place(x=300,y=200)
    for no in nomes:
        li.insert(END,no)


def voltar():
    li.destroy()
    li2.destroy()
    bt4.destroy()
    b3.destroy()
    t1.destroy()
    lins.destroy()
    v.destroy()
    ser()

def d3():
    global lins,v
    torrent = str(ar[nop.index((li2.get(ACTIVE)))])
    lins = Entry(tela,width=80)
    lins.place(x=5,y=420)
    lins.insert(END,torrent)
    v = Button(tela,text="voltar",font="Arial 10 bold",bg="#099",fg="#fff",width=8,command=voltar)
    v.place(x=240,y=450)

def d2():
    global ar,nop,li2,bt4
    na = li.get(ACTIVE)
    li2 = Listbox(tela,width=20,height=10)
    li2.place(x=280,y=80)
    li2.delete(0,END)
    lin = a[ns.index(na)]
    nop = []
    ar = []
    for lai in lin:
        nop.append(lai.text)
        ar.append((str(lai).split('"'))[1])
    li2.delete(0,END)
    for ner in nop:
        li2.insert(END,ner)

    bt4 = Button(tela,text="Download",font="Arial 12 bold",bg="#095",fg="#fff",width=8,command=d3)
    bt4.place(x=352,y=250)


def download():
    global li,t1,b2,a,ns,b3
    nome = li.get(ACTIVE)
    link = (links[nomes.index(nome)])
    pag = bs(requests.get(link).text,"html.parser")
    cont = pag.find_all("div",{"class":"soraddl dlone"})
    ns = []
    a = []
    for c in cont:
        nome = str((c.find("h3")).text)
        a.append(c.find_all("a"))
        ns.append(nome)
    li.destroy()
    t1.destroy()
    b2.destroy()
    li = Listbox(tela,width=40,height=20)
    li.place(x=5,y=80)
    for no in ns:
        li.insert(END,no)

    b3 = Button(tela,text="Ver",font="Arial 12 bold",bg="#098",fg="#fff",width=8,command=d2)
    b3.place(x=252,y=250)
    b1.destroy()
    c1.destroy()
    t1 = Label(tela,text="Conetudo:",font="Arial 12 bold")
    t1.place(x=1,y=50)

def pesquisa():
    mar = str(c1.get())
    if(mar == "" or mar == " "):
        pass
    else:
        url = "https://animestorrent.com/?s="+mar
        inic2(url)

def pesquisa2(t):
    mar = str(c1.get())
    if(mar == "" or mar == " "):
        pass
    else:
        url = "https://animestorrent.com/?s="+mar
        inic2(url)
    
def ser():
    global c1,b1,t1,li,b2
    try:
        c1 = Entry(tela,width=36,font="Arial 14")
        c1.place(x=5,y=10)
        c1.bind("<Return>",pesquisa2)
        b1 = Button(tela,text="Busca",font="Arial 10 bold",bg="#096",fg="#fff",width=7,command=pesquisa)
        b1.place(x=420,y=10)
        t1 = Label(tela,text="Ultimos Adicionados:",font="Arial 12 bold")
        t1.place(x=1,y=50)
        li = Listbox(tela,width=40,height=20)
        li.place(x=5,y=80)
        b2 = Button(tela,text="Ver",font="Arial 12 bold",bg="#098",fg="#fff",width=8,command=download)
        b2.place(x=300,y=200)
        inic()
    except TypeError as erro:
        c1.destroy()
        b1.destroy()
        t1.destroy()
        li.destroy()
        b2.destroy()
        print(erro)
    

def inc():
    global tela
    tela = Tk()
    tela.title("Animes Download")
    tela.geometry("500x500+50+50")
    tela.resizable(FALSE,FALSE)
    ser()
    tela.mainloop()

inc()