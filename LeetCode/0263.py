def isugly(n):
    k=[2,3,5]
    i=0
    while i<len(k):
        if n%k[i]==0:
            n=n/k[i]
            i=0
        else:
            i+=1
        if n==1 or n==0:
            return True
    return False


