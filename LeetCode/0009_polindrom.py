def is_polindrom(x):
    x_0=x
    a=0
    if x<0:
        return False
    while x>0:
        a=a*10
        a+=x%10
        x=x//10
    return x_0==a
print(is_polindrom(1231))