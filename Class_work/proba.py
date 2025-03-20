from random import randint
n=3
matrix=[0]*n
for i in range(n):
    matrix[i]=[0]*n
    for j in range(n):
        matrix[i][j]=randint(0,100)
print(matrix)