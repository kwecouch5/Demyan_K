f=[0]*10000
f[41]=41
for i in range(42,len(f)):
    if i %2==0:
        f[i]=f[i-1]-i
    else:
        f[i]=f[i-2]*i
print(f[9094]//f[9089])