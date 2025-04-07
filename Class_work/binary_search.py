def binary_search(n,target):
    n.sort()
    print(n)
    high=len(n)-1
    low=0
    f=0
    while low<=high:
        mid=(low+high)//2
        if n[mid]<target:
            low=mid+1
        elif n[mid]>target:
            high=mid-1
        else:
            f=mid
            n[mid]+=1
            high = mid - 1
    return f

print(binary_search([1,7,3,2,6,9,4,8,5,4,5,5,5,5,5,5],10))

