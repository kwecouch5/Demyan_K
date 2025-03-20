n=int(input())
cords=[0]*n
for i in range(n):
    cords[i]=int(input())
height=[0]*n
for i in range(n):
    height[i]=int(input())
lies=[0]*n
max_x=height[0]+cords[0]
for i in range(1,n):
    if max_x>=cords[i]:
        lies[i]=1
        max_x=max(max_x,cords[i]+height[i])
    else:
        break
min_x=-height[n-1]+cords[n-1]
for i in range(n-2,0,-1):
    if min_x<=cords[i]:
        lies[i]=1
        min_x=min(min_x,cords[i]+height[i])
    else:
        break
summ=0
for i in range(lies):
    if lies[i]==1:
        summ+=1
print(summ)