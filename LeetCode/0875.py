def minEatingSpeed(piles,h):
    low=1
    high=max(piles)
    while low<high:
        counter=0
        mid=(low+high)//2
        for i in range(len(piles)):
            counter+=piles[i]//mid
            if piles[i]%mid!=0:
                counter+=1
        if counter<=h:
            high=mid
        else:
            low= mid + 1
    return low

print(minEatingSpeed([30,11,23,4,20], h = 6))