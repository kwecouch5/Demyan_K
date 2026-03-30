def SuperRow(a,b):
    bf=''
    for i in range(len(b)):
        bf=bf+str(b[i])
    return (a**int(bf))%1337
print(SuperRow(2,[1,0]))