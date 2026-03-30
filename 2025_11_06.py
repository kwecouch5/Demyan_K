def f(s,h,c=0):
    if s>=61 and h==3:
        return 1
    elif s>=61 and h<3:
        return 0
    elif s<61 and h==3:
        return 0
    if h%2==0:
        f(s+2,h+1,2) or f(s*2,h+1,3)
    else:
        f(s + 2, h + 1, 2) or f(s * 2, h + 1, 3)
print([i for i in range(1,59) if f(i,1,0)])