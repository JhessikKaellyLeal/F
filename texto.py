class Texto():
    def __init__(self,tipo,efeito,texto):
        self.tipo = tipo
        self.efeito = efeito
        self.texto = texto
    def es(self):
        if(self.tipo == 1):
            n = len(self.texto)
            ef = self.efeito * (n + 2)
            msg = "{} \n {} \n{}".format(ef,self.texto,ef)
            print(msg)
        if(self.tipo == 2):
            n = len(self.texto)
            ef = self.efeito * (n + 4)
            text = "{} {} {}".format(self.efeito,self.texto,self.efeito)
            msg = "{}\n{} \n{}".format(ef,text,ef)
            print(msg)
