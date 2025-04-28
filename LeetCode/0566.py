def m_to_dif_m(matrix, n,m):
    if len(matrix)*len(matrix[0])!=m*n:
        return matrix
    matrix_fin = [0] * n
    for i in range(n):
        matrix_fin[i] = [0] * m
    k=0
    l=0
    for i in range(len(matrix_fin)):
        for j in range(len(matrix_fin[0])):
            matrix_fin[i][j]=matrix[k][l]
            l+=1
            if l==len(matrix[0]):
                k+=1
                l=0
    return matrix_fin
print(m_to_dif_m([[1,2,5],[3,4,6]],6,1))