from tkinter import *
from PIL import Image,ImageTk
import qrcode

tela = Tk()
tela.geometry("500x500")
tela.title("Teste")
images = ImageTk.PhotoImage((qrcode.make("teste").get_image()))
im = Label(tela,image=images)
im.pack()
tela.mainloop()