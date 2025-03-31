def setZeroes(matrix):
    l=[]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==0:
                l.append([i,j])
    for i in range(len(l)):
        for j in range(len(matrix)):
            matrix[j][l[i][1]]=0
        for k in range(len(matrix[0])):
            matrix[l[i][0]][k]=0
    print(matrix)
print(setZeroes([[1,1,0],[1,1,1],[1,1,1]]))
