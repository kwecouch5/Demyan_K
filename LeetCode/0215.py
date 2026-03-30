def findKthLargest(nums,k):
    d=[0]*(max(nums)+1-min(nums))
    for i in range(len(nums)):
        a=nums[i]
        if d[a-min(nums)]==0:
            d[a-min(nums)]=1
        else:
            d[a-min(nums)]+=1
    for i in range(len(d)-1,0,-1):
        if d[i]>0:
            if k<=d[i]:
                return i-min(nums)
            k=k-d[i]
            d[i]=0

print(findKthLargest([1,1,2,2,3,3,4,5,6,6],6))