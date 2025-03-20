def greates_comon(a,b):
    if a==0 and b==0:
        return (a+b)
    else:
        if a>b:
            greates_comon(a%b,b)
        else:
            greates_comon(a,b%a)
print(greates_comon(12,16))