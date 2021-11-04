from tkinter import *
import random
x1 = 10
y1 = 10
def cor(event):
    lis = ["red","blue","silver","#000","#fff"]
    cor = random.choice(lis)
    if(cor == "#fff"):
        bt1["fg"] = "#000"
    else:
        bt1["fg"] = "#fff"
    bt1["bg"] = cor
def exit1(event):
    exit()
def key(event):
    global x1,y1
    if(event.char == "w"):
        y1 = y1 - 10
    if(event.char == "s"):
        y1 = y1 + 10
    if(event.char == "a"):
        x1 = x1 - 10
    if(event.char == "d"):
        x1 = x1 + 10
    else:
        pass
    if(x1 == 0 or x1 < 0):
        x1 = 1
    if(y1 == 0 or y1 < 0):
        y1 = 1
    if(x1 == 421 or x1 > 421):
        x1 = 421
    if(y1 == 473 or y1 > 473):
        y1 = 473
    bt1.place(x = x1,y = y1)
tela = Tk()
tela.geometry("500x500+10+10")
tela.title("Text Controle")
bt1 = Button(tela,text="personagem",bg="red",fg="#fff")
bt1.place(x = x1,y = y1)
tela.bind("<Key>",key)
tela.bind("<Return>",exit1)
tela.bind("<Key-space>",cor)
tela.mainloop()
