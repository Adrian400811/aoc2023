with open("input.txt") as inpFile:
     inp = set(inpFile.read().split())

numlist = []
for x in inp:
    numcache = []
    for cha in x:
        if cha.isdigit():
            numcache.append(cha)
    numlist.append(int(str(numcache[0])+str(numcache[-1])))
print(sum(numlist))
