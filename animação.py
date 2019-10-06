from tkinter import *
import random
tela = Tk()
x1 = 1
y1 = 1
n = 10
n2 = 10
cor = "silver"
def mov(event):
    global x1
    global y1
    global n,n2
    global bt1
    global cor
    lista = ["red","blue","silver","#096","#000","#fff"]
    x1 = x1 + n
    y1 = y1 + n2
    if(x1 == 1000 or x1 > 1050):
        n = -10
        cor = random.choice(lista)
    if(y1 == 650 or y1 > 700):
        n2 = -10
        cor = random.choice(lista)
    if(x1 == 0 or x1 < 0):
        n = x1 + 10
        cor = random.choice(lista)
    if(y1 == 0 or y1 < 0):
        n2 = y1 + 10
        cor = random.choice(lista)
    tela["bg"] = cor
    bt1["bg"] = cor
    bt1.place(x=x1,y=y1)
    
tela.geometry("1080x720+10+10")
tela.title("--- TEXT ---")
img = PhotoImage(file="15215445.png")
bt1 = Button(tela,image=img,border="0")
bt1.place(x=x1,y=y1)
tela.bind("<Key-Up>",mov)
tela.mainloop()

    
