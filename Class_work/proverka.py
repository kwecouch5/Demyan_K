def proizv_matrix(a,b):
    if len(a[0])!=len(b):
        return False
    c= [0] * len(a)
    for i in range(len(a)):
        c[i] = [0] * len(b[0])
    for i in range(len(c)):
        for j in range(len(c[0])):
            for r in range(len(b)):
                c[i][j]+=(a[i][r])*(b[r][j])
    return c
print(proizv_matrix([[1],[1]],[[2]]))