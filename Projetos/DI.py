import requests
class Img():
    def __init__(self,url,nome,tipo,local):
        self.url = url
        self.nome = nome
        self.tipo = tipo
        self.local = local
    def Download(self):
        img = (requests.get(self.url)).content
        if(self.local != ""):
            aq = open("{}\{}.{}".format(self.local,self.nome,self.tipo),'wb')
        else:
            aq = open("{}.{}".format(self.nome,self.tipo),'wb')
        aq.write(img)
        aq.close()