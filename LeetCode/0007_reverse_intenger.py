def reverse_intengere(x):
    r=0
    while x>0:
        r=r*10
        r=r+(x%10)
        x=x//10
    return r
def reverse_intengere_1(x):
    x_0=x
    if x<0:
        x=x*-1
    x=str(x)
    x=x[::-1]
    x=int(x)
    if x>=2**31-1 or x<=-2**31:
        return 0
    if x_0>=0:
        return x
    else:
        return x*-1
print(reverse_intengere_1(-122232))
