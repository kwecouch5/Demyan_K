def subsetsWithDup(nums):
    def backtrack(index):
        print(current_subset)
        print(result)
        if index == len(nums):
            result.append(current_subset[:])
            return
        current_subset.append(nums[index])
        backtrack(index + 1)
        removed_element = current_subset.pop()
        while index + 1 < len(nums) and nums[index + 1] == removed_element:
            index += 1
        backtrack(index + 1)
    nums.sort()
    result = []
    current_subset = []
    backtrack(0)
    return result
print(subsetsWithDup([1,2,2]))

