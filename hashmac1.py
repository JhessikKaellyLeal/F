import sys
palavra = str(sys.argv[1])
hashs = []
for letra in palavra:
    hashs.append(ord(letra))
has = ""
for i in hashs:
    has = has + str(i)

print(has)