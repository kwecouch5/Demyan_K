def trap(height):
    counter=0
    l=-1
    r=0
    for i in range(max(height)):
        for j in range(len(height)-1):
            if l!=-1:
                break
            if height[j]>i:
                l=j
        for j in range(len(height)):
            if height[j]>i:
                r=j
        print(l,r)
        for k in range(len(height[l:r:])):
            if height[l:r:][k]<=i:
                counter+=1
        print(counter)
        l=-1
        r=0
    return counter
print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))