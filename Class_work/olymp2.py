h=int(input())
m=int(input())
x=int(input())
y=int(input())
c=x+y
y+=1
counter=1
while True:
    print(x,y)
    if y==m:
        y=0
        x+=1
        if x==h:
            x=0
    if x+y==c:
        print(counter)
        break
    y+=1
    counter+=1
