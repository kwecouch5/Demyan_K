def containsDuplicate(nums):
    d=set(nums)
    if len(d)==len(nums):
        return False
    else:
        return True

