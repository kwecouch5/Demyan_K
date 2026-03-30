def trailingZeroes(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    ff=0
    while True:
        if f%10==0:
            ff+=1
            f=f//10
        else:
            return ff
print(trailingZeroes(1))
