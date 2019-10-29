import requests,sys,urllib.request

if(len(sys.argv) > 2):
    if("-u" in sys.argv):
        url = str(sys.argv[int(sys.argv.index("-u")+1)])
    else:
        print("Passe a url!")
        exit()
else:
    exit()

header = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}

while True:
    try:
        requests.get(url,headers=header)
    except:
        pass
    try:
        urllib.request.urlopen(url)
    except:
        pass