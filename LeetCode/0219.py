def containsNearbyDuplicate(nums,k):
    d={}
    for i in range(len(nums)):
        if nums[i] in d:
             if i-d[nums[i]]<=k:
                 return True
             else:
                 d[nums[i]]=i
        else:
            d[nums[i]]=i
        print(d)
    return False
print(containsNearbyDuplicate([1,2,3,1,2,3],2))