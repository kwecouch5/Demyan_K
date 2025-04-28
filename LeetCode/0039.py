def combinationSum(candidates, target):
    matrix=[[] for _ in range(target+1)]
    list=[]
    print(matrix)
    for num in candidates:
        for j in range(candidates[num], target+1):
            if (num+j)//candidates[num]:
                matrix[(num+j)].append([candidates[num]]*(num+j)//candidates[num])
    print(matrix)
print(combinationSum([2,3,6,7],7))