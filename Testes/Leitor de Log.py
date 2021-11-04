loc = str(input("Digite o nome do log: "))
f = ""
t = ""
n = 0
while True:
    arquivo = open("{}.txt".format(loc),'r')
    try:
        f = arquivo.readlines()[n]
        arquivo.close()
        if(t != f):
            t = f
            n = n + 1
            # O print sera uma saida. Ou seja e so subistitur o print por uma variavel
            print(f.replace('\n',''))
    except:
        arquivo.close()
        pass
        
