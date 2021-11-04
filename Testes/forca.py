import os,random

palavras = ["Loja","Game","Filme","Hacker","Teste","Manga","Novo","Mestre","Jogo","Futebool"]
estrutura = """

     __________
     |        |
     |        {}
     |       {}{}{}
     |       {} {}
     |
     |
_________________
"""
n = 0

class Game():
    def __init__(self):
        self.palavra = random.choice(palavras)
        self.estrutura = estrutura.format(" "," "," "," "," "," ")
        self.frase = "{} ".format("_")*len(self.palavra)
        self.usadas = [] 

    def erros(self,n):
        self.n = n
        if(self.n == 0):
            self.estrutura = estrutura.format(" "," "," "," "," "," ")
        elif(self.n == 1):
            self.estrutura = estrutura.format("0"," "," "," "," "," ")
        elif(self.n == 2):
            self.estrutura = estrutura.format("0"," ","|"," "," "," ")
        elif(self.n == 3):
            self.estrutura = estrutura.format("0","/","|"," "," "," ")
        elif(self.n == 4):
            self.estrutura = estrutura.format("0","/","|","\\"," "," ")
        elif(self.n == 5):
            self.estrutura = estrutura.format("0","/","|","\\","/"," ")
        elif(self.n == 6):
            self.estrutura = estrutura.format("0","/","|","\\","/","\\")
        else:
            self.estrutura = estrutura.format(" "," "," "," "," "," ")
        self.p = "{}\n{}\n{}\n".format("Adivinhe a palavra",self.estrutura,"Numero de erros: {}".format(self.n))
        if(n == 6):
            print("Você perdeu!")
            print("A resposta certa era: {}".format(self.palavra))
            exit()
        else:
            pass

    def checker(self,msg):
        global n
        self.msg = msg
        self.f = ""
        if(len(self.msg) == 1):
            if(self.msg in self.palavra):
                self.mr = [self.msg]
                self.usadas.append(msg + " - Certa!")
                for k in range(0,len(self.frase)):
                    self.mr.append(str(self.frase[k]))
                for c in range(0,len(self.palavra)):
                    if(self.palavra[c] == self.mr):
                        self.f = self.f + " " + self.msg
                    else:
                        self.f = self.f + " _"
                self.frase = self.f
            else:
                n = n + 1
                self.usadas.append(msg + " - Errada!")
                self.frase = " _"*len(self.palavra)
        elif(len(self.msg) > 1):
            if(self.msg == self.palavra):
                print("Você ganhou!")
                exit()
            elif(self.frase == self.palavra):
                print("Você ganhou!")
                exit()
            else:
                n = 6
                print("Perdeu!")
                print("A resposta certa era: {}".format(self.palavra))
                exit()
        else:
            n = n + 1
            self.usadas.append(msg + " - Errada!")
            self.frase = " _"*len(self.palavra)

jogo = Game()
while True:
    jogo.erros(n)
    print(jogo.p)
    print(jogo.frase,'\n',jogo.usadas)
    jogo.checker(str(input("Digite uma letra ou chute a palavra: ")))
    try:
        os.system("cls")
    except:
        os.system("clear")

