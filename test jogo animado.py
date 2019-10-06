from tkinter import *

def m(event):
    global x2
    global y2
    if(event.char == 'd'):
        x2 = x2 + i
    if(event.char == 'a'):
        x2 = x2 + o
    if(event.char == 'w'):
        y2 = y2 + o
    if(event.char == 's'):
        y2 = y2 + i
    if(x2 == 760 or x2 > 760):
        x2 = 760
    if(x2 == 1 or x2 < 1):
        x2 = 1
    if(y2 == 480 or y2 > 480):
        y2 = 480
    if(y2 == 1 or y2 < 1):
        y2 = 1
    person.place(x=x2,y=y2)
    

def mov():
    global x1
    global y1
    global cx
    global cy
    x1 = x1 + cx
    y1 = y1 + cy
    if(x1 == mx or x1 > mx):
        cx = o
    if(x1 == 1 or x1 < 1):
        cx = i
    if(y1 == my or y1 > my):
        cy = o
    if(y1 == 1 or y1 < 1):
        cy = i

def impact():
    global x1
    global x2
    global y1
    global y2
    t = x1 + 25
    j = y1 + 15
    k = x2 + 25
    l = y2 + 15
    for m in range(x1,t):
        for m2 in range(y1,j):
            for n in range(x2,k):
                for n2 in range(y2,l):
                    if(m == n and m2 == n2):
                        exit()
    
def ex():
    mov()
    impact()
    n.place(x=x1,y=y1)
    n.after(20,ex)
tela = Tk()
x1 = 0
y1 = 0
x2 = 770
y2 = 470
i = 10
o = -10
cx = 10
cy = 10
mx = 780
my = 480
tela.geometry('800x500+10+10')
tela.title('Animação')
n = Label(tela,text="IO Virus",bg='#096')
n.place(x=x1,y=y1)
person = Label(tela,text="Player",bg="red")
person.place(x=755,y=my)
ex()
tela.bind('<Key>',m)
tela.mainloop()
