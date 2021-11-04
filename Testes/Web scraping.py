import requests
from bs4 import BeautifulSoup as bs
url = 'https://www.pyjobs.com.br/'
f = f'{url}#oportunidades'
site = requests.get(f)
page = bs(site.text,'html.parser')
bx = page.find_all('div',{'class':'card'})
for b in bx:
    t = b.find('h4').text
    print(t)
