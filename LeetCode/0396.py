def maxRotateFunction(nums):
    f=0
    ff=0
    for i in range(len(nums)):
        f+=i*nums[i]
    for i in range(len(nums)):
        ff=f-




        if ff>f:
            f=ff

print(maxRotateFunction([4,3,2,6]))