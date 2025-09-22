def topKFrequent(nums,k):
    a={}
    for i in range(len(nums)):
        if nums[i] in a:
            a[nums[i]]+=1
        else:
            a[nums[i]]=1
    result=[0]*k
    for i in range(len(result)):
        l=max(a,key=a.get)
        result[i]=l
        a[l]=0
    return result
print(topKFrequent([1,1,1,2,2,3],2))