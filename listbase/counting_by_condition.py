def counting_by_condition(multiple,list_of_numb):
    summ=0
    for i in range(len(list_of_numb)):
        if list_of_numb[i]%multiple==0:
            summ+=1
    return summ
print(counting_by_condition(3,[1,0,0,9,5,4,3]))