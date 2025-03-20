def binary_search(nums,target):
    stop=len(nums)-1
    start=0
    while stop>=start:
        mid=(start+stop)//2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            start=mid+1
        elif target < nums[mid]:
            stop=mid-1
    return None

def left_board(nums,target):
    stop = len(nums) - 1
    start = 0
    while stop >= start:
        mid = (start + stop) // 2
        if target == nums[mid]:
            stop = mid -1
        elif target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            stop = mid - 1
    return start-1
print(left_board([1,3,3,3,3,5,7,8],3))
def right_board(nums,target):
    stop = len(nums) - 1
    start = 0
    while stop >= start:
        mid = (start + stop) // 2
        if target == nums[mid]:
            start = mid + 1
        elif target > nums[mid]:
            start = mid + 1
        elif target < nums[mid]:
            stop = mid - 1
    return stop+1
print(right_board([1,3,3,3,3,5,7,8],3))