def hoar_sort(lst):
    if len(lst) <= 1:
        return
    else:
        l = []
        r = []
        b = []
        for i in range(len(lst)):
            if lst[i] < lst[0]:
                l.append(lst[i])
            elif lst[i] == lst[0]:
                b.append(lst[i])
            else:
                r.append(lst[i])
        hoar_sort(l)
        hoar_sort(r)
        n = 0
        for i in l + b + r:
            lst[n] = i
            n += 1


def minSubArrayLen(target, nums):
     nums.sort()
     nums=nums[::-1]
     counter=0
     for i in range(len(nums)):
         if target<=0:
             return counter
         target=target-nums[i]
         counter+=1
     return 0
print(minSubArrayLen(7,[2,3,1,2,4,3]))
