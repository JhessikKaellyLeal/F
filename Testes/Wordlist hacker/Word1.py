import os
os.system("clear")
lista = ['a','b','c','ç','d','e','f','g','h','i','j','l','m','n','o','p','q','t','u','v','w','x','y','z','A','B','C','Ç','D','E','F','G','H','I','J','L','M','N','O','P','Q','T','U','V','W','X','Y','Z','!','@','#','$','%','&','*','0','1','2','3','4','5','6','7','8','9']
print("""                                                                      
                                                                      
                                                                      
                                                                      
       :rii::::::::::::::::::::,:,:,:,:,:,:::,::::::::::i:i:iii:      
      :7:i::::::,:,:,:,,,:,:.,.,,,.,.,.,.,,,,,,:,:,::::::::::iiv,     
      :i:::::,:,:,,,,,,,,,,.,.,,,.,...,.,.,.,,,,,,:,:,:::::::::r:     
      :r::::::,:,,,:,,,,.,,,.,.,.,.,.,.,.,,,,,.:,,,:,:,::::::::r.     
      :i:::::::,:,,.....,.,...,,,,,,,,,,,.,.....,...,,::::::::ir,     
      :r::::::::,.            .,,,.,.,.,.            .,::::::::7,     
      :ri::::::,.:OZ0qNqEqNq85 .,.,,,,:, rM00PNq0q00M7.,::::::i7:     
      :7:i:i::::.:B@B@B@B@B@B@ .,,,,,,,, UB@B@B@@@B@BF :::::::i7,     
      :ri:::::::.,@MGZGZGZGZ@E .:,:,:,:, 7@O8E8Z8ZOO@L :::::i:i7:     
      :7:i:i:i::.:B8kXkXSkSqMN ,,:,:,:,, 7BEFkFXkXXEBL ::::i:ii7,     
      i7iiiii:::,:@GqXXkXFXXBN ,:,:,:,:, 7@qXFXkXSPN@v.:::i:i:i7,     
      :viiiiii:i.:BBZG0Zq0qGBE .,,,,,,., vBGq0qE0E0OBj ::i:iiiiv,     
      i7;iiiiii::i@B@M@MBMB@@G           7@BBMBMBMBB@U.:i:iiiirv:     
      iviii;iiii::ri:i:i:i:::7EOGOGO8O88Zu:i:::::i:iri:iiiiii;iL:     
      ;vriririiii::.,.,..... :@@@@@@@B@B@S .....,.,.,:iiiiiiiirL:     
      iLrrrr;ri;iiiiii::.... :BM8O8OGO8MB2 ....::i:iiiiii;irirrY:     
      rYrr7rrrr;ri;i;ii:7;;i:7@ZEN00EN0EB5:i;i7i::iiiiiiririrrrY:     
      ;ur7r7rrrrr;iri;:vB@B@B@O80Z0ZNZqZ8@@@B@BZ.ii;irir;rrrr77U:     
      rJvr7rrrr;riri;i:r@B@BBMOZGEGZGZ8GOMBB@B@k,irr7r7r7r7777v2:     
      ru77r7r7rr;r;ri;:rBM8888Z8ZOG8Z8EGGOG8GMBk,rr7r7r7777v7vvF:     
      7uv7v7777r7r7rri:r@OOGOG8Z8ZOZ8ZOGOZ8GOO@F:;7r77777777vvL5i     
      75vv7v777777r7r7:7BM8O8OOOOMOOOOOOOOGO8MBX:7r7777v7v7LvLLX:     
      v1Y7v7v7v777777rir@MMOMM@B@B@B@B@B@BMOMO@S:7v7v7vvLvLvLLJXi     
      7kLLvvvv7v7v7777ivBBMMMMSqq0qNPNqNSGMMOMBX:7vLvvvLLYLLLJjNi     
      vFJLLLLvLvvvv7v7;v@BBM@0,:::i:i:::,L@MBM@Xi7LvLvYLYYJYjYuqi     
      vXJJLJLLvLvLvLvv;LB@B@BMi7vvvLvvvviFB@@@BEiLLJLYYjYjJjJuuGi     
      Yq2jYLLvYvLvLvL7rY@B@B@Br7v7v7L7LvrX@B@B@0rLJYLvLLLvYLjLuPi     
      YZ2uLJLJLYLLvLLL7v77r77v7LLLvLLLLYvL77777LLjJuLLLJLYLuYujEi     
      j0FujJjYJLJYJLYLLvv777v7LLYLYLLLjJJLLvLvLYuJuuJLuYjYujuJU0r     
      JO52JuJuJuYJYjLJLYYjYjYJLjYJLJYjjuJuuujuuUuuu2JuYujujuuUU8i     
      uGSUujujujuJuJjYjYujuJujuJuJuYjJuuuuUuUuUuUu22uJUuUu2uUu58r     
      2MSFu2u2u2u2uUuujuUUuUuUuUuUuUjUU121U2U525251Fuuu1U1U1251Mr     
      1BONXkXkPSXFXSkSkFPkkkkSXFXSXSkSqXqXqXqXNPqPNqXSPkPkqXPPZBr     
       1OM0Z0Z0EqEN0q0q0EZ0ZNZ0Z0E0ENEEGEGE8E8ZGZ8ZO0E0E0Z0ZZOEL



       """)

print("""

]--> 1) Gera wordlist padrão com todas as posiblilidades de 8 caracteris.

]--> 2) Criar wordlist personalizada.

""")
def Gera():
    Local = input("Digite o local mais o nome do arquivo e .txt (exemplo: /sdcard/word.text): ")
    l = 0
    w = 0
    j = 0
    k = 0
    f = 0
    g = 0
    h = 0
    i = 0
    arquivo = open(Local,'w')
    print('Loading... ')
    for a in range(9999999999999999999999999999999999999999999999999999999):
        texto = str(lista[l]+lista[w]+lista[j]+lista[k]+lista[f]+lista[g]+lista[h]+lista[i]+'\n')
        arquivo.write(texto)
        i = i + 1
        if(i == 65):
            i = 0
            h = h +1
        if(h == 65):
            h = 0
            g = g + 1
        if(g == 65):
            g = 0
            f = f + 1
        if(f == 65):
            f = 0
            k = k + 1
        if(k == 65):
            k = 0
            j = j + 1
        if(j == 65):
            j = 0
            w = w + 1
        if(w == 65):
            w = 0
            l = l +1
        if(l == 65):
            print('Concluido !')
            break

def persona():
    a = int(0)
    Local = input("Digite o local mais o nome do arquivo e .txt (exemplo: /sdcard/word.text): ")
    arquivo = open(Local,'w')
    for a in range(9999999999999999999999999999999):
        a = a + 1
        te = str(input("Digite o iten da wordlist no final colorque(para sair digite exe): "))
        if (te == "exe"):
            arquivo.close()
            break
        te = te + '\n'
        print(te)
        arquivo.write(te)
        
n1 = int(input("]--> "))
if (n1 == 1):
    Gera()
if (n1 == 2):
    persona()
           
