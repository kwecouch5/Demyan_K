def generateMatrix(n):
    matrix = [0] * n
    for i in range(n):
        matrix[i] = [0] * n
    x_0=0
    y_0=0
    x_1=n-1
    y_1=n-1
    counter=1
    while counter<=n**2:
        i=x_0
        while i<=x_1 and counter<=n**2:
            matrix[y_0][i]=counter
            i+=1
            counter+=1
        j=y_0+1
        while j<=y_1-1 and counter<=n**2:
            matrix[j][x_1]=counter
            j+=1
            counter+=1
        i = x_1
        while i >= x_0 and counter <= n ** 2:
            matrix[y_1][i] = counter
            i -= 1
            counter += 1
        j = y_1-1
        while j >= y_0+1 and counter <= n ** 2:
            matrix[j][x_0] = counter
            j -= 1
            counter += 1
        x_0 += 1
        y_0 += 1
        x_1 -= 1
        y_1 -= 1
    return matrix
print(generateMatrix(4))