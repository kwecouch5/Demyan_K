def fib(n):
    f=[0]*(n+1)
    for i in range(len(f)):
        if i<=1:
            f[i]=1
        else:
            f[i]=f[i-1]+f[i-2]
    return f[n-1]
print(fib(3))