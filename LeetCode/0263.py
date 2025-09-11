def isugly(n):
    if n==0:
        return False
    k=[2,3,5]
    i=0
    while i<len(k):
        if n%k[i]==0:
            n=n/k[i]
            i=0
        else:
            i+=1
        if n==1:
            return True
    return False


