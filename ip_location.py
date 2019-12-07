from bs4 import BeautifulSoup as bs
import requests,sys

if(len(sys.argv) > 1):
    if("-i" in sys.argv):
        ip = str(sys.argv[sys.argv.index("-i")+1])
    else:
        print("Passe o ip com -i [IP] ou execulte o arquivo e espere a solicitação do ip!")
        exit()
else:
    ip = str(input("Digite o ip: "))
try:
    print("\n")
    head = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    pagina = bs(requests.get("https://ipapi.com/ip_api.php?ip={}".format(ip),headers=head).text,"html.parser")
    cont = str(pagina).replace("{","")
    cont = cont.replace("}","")
    cont = cont.replace("'","")
    cont = cont.replace('"',"")
    cont = cont.split(",")
    for c in range(0,13):
        try:
            print(cont[c])
        except:
            pass

except:
    pass
