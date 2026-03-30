a=18*7**107-5*49**76+345**35-50
c=0
a=abs(a)
for i in range(1, 30):
    if a == 0:
        break
    c += a % (49 ** i)
    a = a // (49 ** i)
print(c)