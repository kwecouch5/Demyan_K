def integerReplacement(n):
    counter=0
    while n!=1:
        if n%2==0:
            n=n//2
        else:
            if (n+1)%4==0 and (n-1)//2>1:
                n+=1
            else:
                n-=1
        counter+=1
    return counter
print(integerReplacement(7))
