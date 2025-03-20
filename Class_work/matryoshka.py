def matryoshka(n):
    if n==1:
        print('Matryoshechka')
    else:
        print('Верх матрешки', n)
        matryoshka(n-1)
        print('Низ матрешки',n)
matryoshka(6)