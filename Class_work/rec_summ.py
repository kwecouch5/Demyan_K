def summ_lst_rec(l):
    if len(l) == 0:
        return 0
    else:
        return l[0]+summ_lst_rec(l[1::])
print(summ_lst_rec([1,2,3,4,5,6,7,8,9]))