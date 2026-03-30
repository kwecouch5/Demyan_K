def findSubstringInWraproundString(s):
    a=[0]*len(s)
    b=[0]*len(s)
    ser=set()
    for i in range(len(s)):
        a[i]=ord(s[i])-ord('a')
    b[0]=1
    k=''
    for i in range(1, len(b)):
        if a[i]-a[i-1]==1 or a[i]-a[i-1]==-25:
            b[i]=b[i-1]+1
        else:
            b[i]=1
        h=int(a[i])
        for j in range(b[i]):
            k+=str(h)
            if h==0:
                h=25
            else:
                h-=1
            ser.add(k)
        k=''
    return len(ser)
print(findSubstringInWraproundString("uvwxyzabcdefg"))