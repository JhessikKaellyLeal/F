import pandas,sys

if(len(sys.argv) > 2):
    if("-l" in sys.argv):
        l = str(sys.argv[sys.argv.index("-l")+1]).split(',')
        l = sorted(l)
    else:
        print("E obrigatorio declarar a lista de numero exemplo: -l 1,2,3,4,5,6,7,8,9,20,50 ")
        exit()
    if("-class" in sys.argv):
        classe = int(sys.argv[sys.argv.index("-class")+1])
    else:
        classe = 4
    amplitude = int(l[len(l)-1]) - int(l[0])
    intervalo = amplitude / classe
    inter_list_print = []
    quantidade = []
    quantidade_acumulativa = []
    porcen = []
    porcen_acumulativa = []
    final = []
    atual = int(l[0])
    for i in range(0,classe):
        proximo = atual + intervalo
        intervalo_list_print = f"{str(int(atual))} |----- {str(int(proximo))}"
        intervalo_list = range(int(atual),int(proximo))
        atual = proximo
        inter_list_print.append(intervalo_list_print)
        quan = 0
        for q in l:
            if(int(q) in intervalo_list):
                quan = quan + 1
            else:
                pass
        quantidade.append(quan)
    quantidade[len(quantidade)-1] = quantidade[len(quantidade)-1]+1
    qc = 0
    for qu in quantidade:
        qc = qc+qu
        quantidade_acumulativa.append(qc)

    for qa in quantidade:
        porcen.append((qa/len(l))*100)

    por = 0
    for p in porcen:
        por = por + p
        porcen_acumulativa.append(por)
        
    for num in range(0,classe):
        final.append([inter_list_print[num],quantidade[num],quantidade_acumulativa[num],porcen[num],porcen_acumulativa[num]])

    print(pandas.DataFrame(data=final,columns=["variações","fi","Fi","fr %","FRi %"]))
else:
    print("Para usar tem que declar a lista de numero(obigatorio), exemplo: -l 1,2,3,4,5,6,7,8,9,20,50\nE também pode se passar o numero de classes(linha que a tabela vai ter), exemplo: -class 4")