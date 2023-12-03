with open("day1input.txt") as inpFile:
     inp = set(inpFile.read().split())

dig = []
for tester in inp:
    numcache = []
    numcount = 0
    try:
        print(tester)
        for cha in tester:
            if not cha.isdigit():
                if cha == "o":
                    if tester[numcount+1] == "n":
                        if tester[numcount+2] == "e":
                            numcache.append("1")

                if cha == "t":
                    if tester[numcount+1] == "w":
                        if tester[numcount+2] == "o":
                            numcache.append("2")
                    if tester[numcount+1] == "h":
                        if tester[numcount+2] == "r":
                            if tester[numcount+3] == "e":
                                if tester[numcount+4] == "e":
                                    numcache.append("3")

                if cha == "f":
                    if tester[numcount+1] == "o":
                        if tester[numcount+2] == "u":
                            if tester[numcount+3] == "r":
                                numcache.append("4")
                    if tester[numcount+1] == "i":
                        if tester[numcount+2] == "v":
                            if tester[numcount+3] == "e":
                                numcache.append("5")

                if cha == "s":
                    if tester[numcount+1] == "i":
                        if tester[numcount+2] == "x":
                            numcache.append("6")
                    if tester[numcount+1] == "e":
                        if tester[numcount+2] == "v":
                            if tester[numcount+3] == "e":
                                if tester[numcount+4] == "n":
                                    numcache.append("7")

                if cha == "e":
                    if tester[numcount+1] == "i":
                        if tester[numcount+2] == "g":
                            if tester[numcount+3] == "h":
                                if tester[numcount+4] == "t":
                                    numcache.append("8")

                if cha == "n":
                    if tester[numcount+1] == "i":
                        if tester[numcount+2] == "n":
                            if tester[numcount+3] == "e":
                                numcache.append("9")



            if cha.isdigit(): #count ints in digit
                numcache.append(cha)
            numcount += 1


    print(numcache)
