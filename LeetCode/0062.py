def uniquePaths(m,n):
    matrix=[]
    for i in range(n):
        matrix.append([0]*m)
    for i in range(m):
        matrix[0][i]=1
    for i in range(n):
        matrix[i][0]=1
    for j in range(n-1):
        for i in range(m-1):
            matrix[j+1][i+1]=matrix[j][i+1]+matrix[j+1][i]
    return matrix[n-1][m-1]

print(uniquePaths(7,3))