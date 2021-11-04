from tkinter import *
import random
import time
def resolution(op):
    if(op == 1):
        return("1080x720+10+10")
    if(op == 2):
        return("500x400+10+10")
def t1():
    x=10
    y=50
    return(x,y)
def Neg():
    x=10000
    y=10000
    return(x,y)
def Mode():
    text1x,text1y = Neg()
    text1.place(x = text1x,y = text1y)
def Mode1():
    text1x,text1y = t1()
    text1.place(x = text1x,y = text1y)
def Mode2():
    lista = [10,20,30,40,50,60,90,100,300,350]
    text1.place(x = random.choice(lista),y = random.choice(lista))
tela = Tk()
tela.geometry(resolution(2))
tela.title("TEXT return")
text1x,text1y = t1()
text1 = Label(tela,text = "Usuario: ")
text1.place(x = text1x,y = text1y)
bt = Button(tela,text="mode",command = Mode)
bt.place(x = 100,y = 100)
bt1 = Button(tela,text="mode1",command = Mode1)
bt1.place(x = 100,y = 120)
bt1 = Button(tela,text="mode2",command = Mode2)
bt1.place(x = 100,y = 140)
tela.mainloop()
