def generate(numRows):
    triangle=[0]*numRows
    for i in range(numRows):
        triangle[i]=[0]*(i+1)
    for i in range(len(triangle)):
        triangle[i][0]=1
        triangle[i][len(triangle[i]) - 1] = 1
    for i in range(len(triangle)):
        for j in range(len(triangle[i])):
            if triangle[i][j]==0:
                triangle[i][j]=triangle[i-1][j-1]+triangle[i-1][j]
    return triangle
print(generate(5))