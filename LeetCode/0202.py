def is_happynumber(n):
    d={}
    sum_1=0
    while True:

        while n>0:
            sum_1+=(n%10)**2
            n=n//10
        if sum_1 in d:
            return False
        elif sum_1 == 1:
            return True
        else:
            d[sum_1]=1
        n=sum_1
        sum_1=0
print(is_happynumber(12))
