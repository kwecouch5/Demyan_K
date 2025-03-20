def fibanachi(n):
    if n==2 or n==1:
        return 1
    else:
        return fibanachi(n-1)+fibanachi(n-2)
print(fibanachi(40))