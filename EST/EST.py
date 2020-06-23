classes = int(input("Numero de classes: "))
cs = classes + 1
classe = []
fi = []
for c in range(1,cs):
    classe.append(str(input("classe {}: ".format(c))))
    fi.append(float(input("valor da classe {}: ".format(c))))

sfi = 0
for f in fi:
    sfi = sfi + f

Fi = []
n2 = 0
for m in range(0,classes):
    n1 = fi[m]
    Fi.append(n1 + n2)
    n2 = n1 + n2

mi = []
for c in range(0,classes):
    c1 = classe[c].replace("|","")
    c1 = c1.replace("-","")
    pmi = c1.split()
    mi.append((int(pmi[0])+int(pmi[1]))/2)


fimi = []
for f in range(0,classes):
    fimi.append(fi[f] * mi[f])

sfimi = 0
for s in fimi:
    sfimi = sfimi + s

x = sfimi/sfi

sumix = []
for m in mi:
    sumix.append(m - x)

sf = 0
for i in range(0,classes):
    sf = sf + ((sumix[i])**2)*fi[i]

arquivo = open("resultado.txt","w")
arquivo.write("\nclasses | fi | Fi | mi | fi*mi | x | mi-x | (mi-x)**2 | ((mi-x)**2)*fi\n")
for r in range(0,classes):
    arquivo.write("{} | {} | {} | {} | {} | {} | {} | {} | {}\n".format(classe[r],fi[r],Fi[r],mi[r],fimi[r],x,sumix[r],(sumix[r])**2,((sumix[r])**2)*fi[r]))

arquivo.write("  soma de fi ({}) | soma de fi*m1 ({}) | soma de ((mi-x)**2)*fi ({})| S ({}) | (sf/(sfi-1))**(1/2)) ({})".format(sfi,sfimi,sf,sf/(sfi-1),(sf/(sfi-1))**(1/2)))
arquivo.close()