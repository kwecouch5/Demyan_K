f=[0]*10010
for i in range(len(f)-1,1,-1):
    if i>10000:
        f[i]=42
    elif i%2==0:
        f[i]=2*i+f[i+3]+f[i+4]+f[i+6]
    else:
        f[i]=-(i+f[i+1]+f[i+3])
print(f[9996]-f[9994])
print(f)