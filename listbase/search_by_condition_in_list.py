def is_name(name,name_lst):
    for i in range(len(name_lst)):
        if name==name_lst[i]:
            print('Имя есть')
            return True
    print('Имени нет')
    return False
print(is_name('Dd',['ss','sd','Ds']))