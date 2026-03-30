def minMutation(startGene,endGene,bank):
    if len(bank)==0:
        return -1
    s=0
    for i in range(len(startGene)):
        if startGene[i]!=endGene[i]:
            s+=1
    return s

