def Stepan(n):
    n_0=str(n)
    fin=[]
    f=0
    for i in range(len(n_0)//2+1):
        if f==0:
            f+=1
        elif n_0[i]!='0':
            num_1 = n_0[:i:]
            num_2 = n_0[i::]
            num_2=int(num_2)
            num_1=int(num_1)
            if num_2>= num_1:
                fin.append([num_1, num_2])
            else:
                break
    return fin
print(Stepan(12345678))