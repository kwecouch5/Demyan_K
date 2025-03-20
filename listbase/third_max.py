def third_max(nums):
    first = second = third = float('-inf')
    for num in nums:
        if num > first:
            third = second
            second = first
            first = num
        elif first > num > second:
            third = second
            second = num
        elif second > num > third:
            third = num

    return third
print(third_max([1,6,2,7,3,6,12,14]))