def threeSumClosest(nums, target):
    nums.sort()
    fin_result=[]
    print(nums)
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        i_2=i+1
        i_3=len(nums)-1
        while i_2<i_3:
            result=nums[i]+nums[i_2]+nums[i_3]
            fin_result.append(result)
            if result==target:
                return result
            elif result>target:
                i_2+=1
            elif result<target:
                i_3-=1
    print(fin_result)
    for j in range(len(fin_result)):
        fin_result[j]-=target
        if fin_result[j]<0:
            fin_result[j]=fin_result[j]*-1
    return min(fin_result)


print(threeSumClosest([1,2,3,4,5,6,7,2,1,14,2,114], 3))
