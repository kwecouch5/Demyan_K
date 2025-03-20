def threeSum(nums):
    nums.sort()
    fin_result=[]
    for i in range(len(nums)-2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        i_2=i+1
        i_3=len(nums)-1
        while i_2<i_3:
            result=nums[i]+nums[i_2]+nums[i_3]
            if result==0:
                fin_result.append([nums[i],nums[i_2],nums[i_3]])
                i_2+=1
                i_3+=-1
                while nums[i_2] == nums[i_2- 1] and i_2 < i_3:
                    i_2 += 1
                while i_2 < i_3 and nums[i_3] == nums[i_3+1]:
                    i_3 +=-1
            elif result>0:
                i_3+=-1
            elif result<0:
                i_2+=1
    return fin_result
print(threeSum([1,0,1,2,-2,0]))