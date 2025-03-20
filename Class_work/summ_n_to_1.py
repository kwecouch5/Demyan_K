def summ_n_to_1(n):
    if n==1:
        return 1
    else:
        return n+summ_n_to_1(n-1)
print(summ_n_to_1(6))