def countBits(n):
    l=[0]*(n+1)
    for i in range(len(l)):
        l[i]=bin(i)[2::].count('1')
    return l
print(countBits(5))
