def g(x,h):
    if x>41 and (h==3 or h==5):
        return 1
    elif h==5 and x<42:
        return 0
    elif x>41 and h<5:
        return 0
    else:
        if h%2==0:
            return g(x+1,h+1) or g(x+3,h+1) or g(x*2,h+1)
        else:
            return g(x+1,h+1) and g(x+3,h+1) and g(x*2,h+1)
for x in range(1,42):
    if g(x,1)==1:
        print(x)
