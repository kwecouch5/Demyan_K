def sortColors(nums):
    k_0=0
    k_1=0
    k_2=0
    for i in range(len(nums)):
        if nums[i]==0:
            k_0+=1
        elif nums[i]==1:
            k_1+=1
        else:
            k_2+=1
    i=0
    while k_2!=0 or k_0!=0 or k_1!=0:
        if k_0!=0:
            nums[i]=0
            i+=1
            k_0-=1
        elif k_1!=0:
            nums[i]=1
            i+=1
            k_1-=1
        else:
            nums[i]=2
            i+=1
            k_2-=1
    print(nums)
print(sortColors([1,0]))