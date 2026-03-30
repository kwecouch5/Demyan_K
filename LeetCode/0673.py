from itertools import count


def findNumberOfLIS(nums):
    f_dp=[1]*len(nums)
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                if dp[j]+1>dp[i]:
                    dp[i] = dp[j] + 1
                    f_dp[i] = f_dp[j]
                elif dp[i]==dp[j]+1:
                    f_dp[i] += f_dp[j]
    y=max(dp)
    result=0
    for i in range(len(dp)):
        if dp[i]==y:
            result+=f_dp[i]
    return result
print(findNumberOfLIS([1,1,1,2,2,2,3,3,3]))