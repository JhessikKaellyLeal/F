class Texto():
    def __init__(self,efeito,texto,carac):
        self.efeito = efeito
        self.texto = texto
        self.carac = carac
    def Tes(self):
        if(self.efeito == 1):
            n = len(self.texto)
            m = self.carac * (n + 4)
            print("{}\n  {}\n{}".format(m,self.texto,m))
        if(self.efeito == 2):
            n = len(self.texto)
            m = self.carac * (n + 4)
            m1 = "{} {} {}".format(self.carac,self.texto,self.carac)
            print("{}\n{}\n{}".format(m,m1,m))
        if(self.efeito == 3):
            n = len(self.texto)
            m = self.carac * (n + 4)
            msg = "{} {} {}".format(self.carac,self.texto,self.carac)
            print("{}\n{}\n{}\n{}\n{}".format(m,m,msg,m,m))