a='АЕКПТЧ'
c=0
for x in a:
    for y in a:
        for w in a:
            for z in a:
                for g in a:
                    for p in a:
                        for u in a:
                            l=x+y+w+z+g+p+u
                            c+=1
                            if l=='АПТЕЧКА':
                                uu=c
                            if l=='ПЕЧАТКА':
                                uuu=c
                                print(uuu-uu)