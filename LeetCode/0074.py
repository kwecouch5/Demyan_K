def searchMatrix(matrix,target):
    high = len(matrix) - 1
    low = 0
    m_1=-1
    while low<=high:
        mid=(low+high)//2
        if matrix[mid][len(matrix[0])-1]<target:
            low=mid+1
        elif matrix[mid][0]>target:
            high=mid-1
        else:
            m_1=mid
            break
    print(matrix[m_1])
    low_s=0
    high_s=len(matrix[m_1])-1
    while low_s<=high_s:
        mid_s=(low_s+high_s)//2
        if matrix[m_1][mid_s]<target:
            low_s=mid_s+1
        elif matrix[m_1][mid_s]>target:
            high_s=mid_s-1
        else:
            return True
    return False
print(searchMatrix([[1],[3]], target =3))

