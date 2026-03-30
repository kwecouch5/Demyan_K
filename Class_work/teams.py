def teems(teams,stradiums):
    stadium_1 = teams
    stadium_2 = teams
    stadium_3 = teams
    stadium_4 = teams
    stadium_5 = teams
    stadium_6 = teams
    tour_1 = []
    tour_2 = []
    tour_3 = []
    tour_4 = []
    tour_5 = []
    tour_6 = []
    final=[]
    c=[]
    k=0
    i=0
    for j in range(len(teams)-7):
        while k!=2:
            final.append(stadium_1[i])
            c.append(stadium_1[i])
            stadium_1.
        i=0
        while k!=2:
            if stadium_2[i] not in c:
                final.append(stadium_2[i])
                c.append(stadium_2[i])
                i+=1
                k+=1
            else:
                i+=1
        i = 0
        k=0
        while k != 2:
            if stadium_3[i] not in c:
                final.append(stadium_3[i])
                c.append(stadium_3[i])
                i += 1
                k += 1
            else:
                i += 1
        i = 0
        k=0
        while k != 2:
            if stadium_4[i] not in c:
                final.append(stadium_4[i])
                c.append(stadium_4[i])
                i += 1
                k += 1
            else:
                i += 1
        i = 0
        k=0
        while k != 2:
            if stadium_5[i] not in c:
                final.append(stadium_5[i])
                c.append(stadium_5[i])
                i += 1
                k += 1
            else:
                i += 1
        i = 0
        k=0
        while k != 2:
            if stadium_6[i] not in c:
                final.append(stadium_6[i])
                c.append(stadium_6[i])
                k += 1
                i += 1
            else:
                i += 1
        print(final)
        if j==0:
            tour_1=final
        elif j==1:
            tour_2=final
        elif j == 2:
            tour_3 = final
        elif j == 3:
            tour_4 = final
        elif j==4:
            tour_5=final
        elif j==5:
            tour_6=final
print(teems([1,2,3,4,5,6,7,8,9,10,11,12],6))