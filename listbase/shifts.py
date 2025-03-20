def is_left_shift(lst):
    zero_el=lst[0]
    for i in range(len(lst)-1):
        lst[i]=lst[i+1]
    lst[len(lst)-1]=zero_el
    return lst
def is_right_shift(lst):
    return lst[-1:] + lst[:-1]
def is_shift(lst,shft=1):
    if shft==1:
        zero_el = lst[0]
        for i in range(len(lst) - 1):
            lst[i] = lst[i + 1]
        lst[len(lst) - 1] = zero_el
        return lst
    else:
        return lst[-1:] + lst[:-1]
def is_shift_slice_r(lst,shift=1):
    return lst[-shift:] + lst[:-1]
def is_shift_slice_l(lst,shift=1):
    return  lst[shift:] + lst[:shift]
print(is_shift_slice_l([1,2,3,4,5,6,7,8,9],3))