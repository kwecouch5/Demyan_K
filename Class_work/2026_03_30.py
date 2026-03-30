def game(x,y,h):
    if x+y>=75 and h==2:
        return 1
    elif x+y>=75 and h<2:
        return 0
    elif x+y<75 and h==2:
        return 0
    else:
        if h%2==0:
            return game(x+y,y,h+1) or game(x+1,y,h+1) or game(x,y+x,h+1) or game(x,y+1,h+1)
        else:
            return game(x + y, y, h + 1) or game(x + 1, y, h + 1) or game(x, y + x, h + 1) or game(x, y + 1, h + 1)
for s in range(1,68):
    if game(s,7,0)==1:
        print(s)