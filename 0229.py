def majorityElement(nums):
    d=dict()
    b=[]
    for i in range(len(nums)):
        if nums[i] in d:
            d[nums[i]]+=1
        else:
            d[nums[i]]=1
    for num,count in d.items():
        if count>len(nums)//3:
            b.append(num)
    return b
print(majorityElement([3,2,2]))