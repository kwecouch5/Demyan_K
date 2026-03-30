m=9999999999999
for n in range(483,1000):
    r=oct(n)[2::]
    r=str(r)
    s=0
    for i in range(len(r)):
        s+=int(r[i])

    if s%2==0:
        s=oct(s)[2::]
        r=r+str(s)
    else:
        s=oct(s)[2::]
        r=str(s)+r
    rr=int(r,8)
    m=min(m,rr)
print(m)