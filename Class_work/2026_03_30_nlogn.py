def merge(l, r):
    s=[0]*(len(l)+len(r))
    i_l=0
    i_r=0
    i_s=0
    while i_l < len(l) and i_r < len(r):
        if l[i_l]>=r[i_r]:
            s[i_s]=r[i_r]
            i_r+=1
            i_s+=1
        else:
            s[i_s]=l[i_l]
            i_l+=1
            i_s+=1
    while i_l<len(l):
        s[i_s]=l[i_l]
        i_s+=1
        i_l+=1
    while i_r<len(r):
        s[i_s]=r[i_r]
        i_s+=1
        i_r+=1
    return s

def lognsort(n):
    if len(n)<=1:
        return n
    else:
        l=len(n)//2
        p1=lognsort(n[:l:])
        p2=lognsort(n[l::])
        final=merge(p1,p2)
        for i in range(len(n)):
            n[i]=final[i]
        return n
a=[1,3,5,7,9,2,4,8,6,10,14]
lognsort(a)
print(a)