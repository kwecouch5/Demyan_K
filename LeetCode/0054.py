def spiral_matrix(matrix):
    x=len(matrix[0])
    y=len(matrix)
    x_0=0
    y_0 = 0
    x_1=x-1
    y_1=y-1
    fin=[]
    while len(fin) < x*y:
        i=x_0
        while i <= x_1 and len(fin) < x*y:
            fin.append(matrix[y_0][i])
            i+=1
        j=y_0+1
        while j <= y_1-1 and len(fin) < x*y:
            fin.append(matrix[j][x_1])
            j+=1
        i=x_1
        while i >= x_0 and len(fin) < x*y:
            fin.append(matrix[y_1][i])
            i-=1
        j=y_1-1
        while j >= y_0+1 and len(fin) < x*y:
            fin.append(matrix[j][x_0])
            j-=1
        x_0+=1
        y_0+=1
        x_1-=1
        y_1-=1
    return fin
print(spiral_matrix([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))