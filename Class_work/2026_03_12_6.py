f=[0]*3050
f[0]=1
f[1]=1
f[2]=1
for i in range(4,len(f)):
    if i%2==0:
        f[i]=f[i-1]+i-1
    else:
        f[i]=f[i-2]+2*i-2
print(f[3048]-f[3045])