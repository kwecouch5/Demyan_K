def nthUglyNumber(n):
    if n==1:
        return 1
    for i in range(1,(n**3)+1):
        if n==0:
            return g
        pr=0
        g=i
        while True:
            if i==pr:
                break
            elif i==1:
                n-=1
                break
            pr=i
            if i%2==0:
                i=i//2
            elif i%3==0:
                i=i//3
            elif i % 5 == 0:
                i = i // 5
print(nthUglyNumber(1))