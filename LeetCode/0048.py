def rotate(matrix):
    for i in range(len(matrix)//2):
        matrix[i],matrix[len(matrix)-(i+1)]=matrix[len(matrix)-(i+1)], matrix[i]
    for i in range(len(matrix)):
        for j in range(len(matrix)-i):
            matrix[i][j+i],matrix[j+i][i]=matrix[j+i][i],matrix[i][j+i]
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print(matrix[i][j], end=' ')
        print()

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))