def n_to_1(n):
    if n<2:
        print(n)
        return 1
    else:
        n_to_1(n-1)
        print(n)
n_to_1(8)