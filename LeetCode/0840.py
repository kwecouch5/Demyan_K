def magicsquare(matrix):
    k=matrix[0][0]+matrix[0][1]+matrix[0][2]
    for i in range(len(matrix)):
        if matrix[i][0]+matrix[i][1]+matrix[i][2]!=k:
            return 0
        if matrix[0][i]+matrix[1][i]+matrix[2][i]!=k:
            return 0
    if matrix[0][0]+matrix[1][1]+matrix[2][2]!=k:
        return 0
    if matrix[0][2]+matrix[1][1]+matrix[2][0]!=k:
        return 0
    return 1
print(magicsquare([[4,3,8],[9,5,1],[2,7,6]]))
