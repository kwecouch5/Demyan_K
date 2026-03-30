def f(s,h):
    if s<=19 and h==3:
        return 1
    elif s<=19 and h<3:
        return 0
    elif s>19 and h==3:
        return 0
    else:
        if h % 2 == 0:
            return f(s - 2, h + 1) or f(s - 5, h + 1) or f(s // 3, h + 1)
        else:
            return f(s - 2, h + 1) or f(s - 5, h + 1) or f(s // 3, h + 1)
for i in range(20,100):
    if f(i,1)==1:
        print(i)