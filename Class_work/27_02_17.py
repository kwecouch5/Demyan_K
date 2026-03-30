a=open('17_27.txt')
d=[]
c=0
m=999999999999999999
for s in a:
    d.append(int(s))
for i in range(2,len(d)-3):
    o=[]
    p=9999999999999999999999
    if d[i]+d[i+1]>d[i-2]+d[i-1] and d[i]+d[i+1]>d[i+2]+d[i+3]:
        if d[i]+d[i+1]>0 and d[i-2]+d[i-1]>0 and d[i+2]+d[i+3]>0:
            c+=1
            o.append(d[i]*d[i+1])
            o.append(d[i-2] * d[i - 1])
            o.append(d[i+2] * d[i + 3])
            p=min(o)
    m=min(p,m)
print(c,m)