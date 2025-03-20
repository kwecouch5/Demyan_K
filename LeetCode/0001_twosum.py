def twoSum_0(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i]+nums[j]==target and i!=j:
                return [i,j]

def twoSum(nums,target):
    d={}
    for i in range(len(nums)):
        a=target-nums[i]
        if a in d:
            return [d[a],i]
        else:
            d[nums[i]]=i
print(twoSum([2,7,8,2],4))