with open("day2input.txt") as inpFile:
     inp = [line.strip() for line in inpFile]

gameid = []
gidcount = 0
for x in inp:
    gidcount += 1
    r,g,b = 0,0,0
    inpcache = []
    for y in x.split(", "):
        for z in y.split("; "):
            for aa in z.split(": "):
                inpcache.append(aa)

    for ab in inpcache:
        if ab[2] == 'r':
            ac = ab.split(" ")
            r += int(ac[0])
        elif ab[2] == 'g':
            ac = ab.split(" ")
            g += int(ac[0])
        elif ab[2] == 'b':
            ac = ab.split(" ")
            b += int(ac[0])

    if r<=12 and g<=13 and b<=14:
        print(f"r{r}g{g}b{b}gid{gidcount}")
        gameid.append(gidcount)

print(sum(gameid))
