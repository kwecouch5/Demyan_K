def hoar_sort(lst):
    if len(lst)<=1:
        return
    else:
        l=[]
        r=[]
        b=[]
        for i in range(len(lst)):
            if lst[i]<lst[0]:
                l.append(lst[i])
            elif lst[i]==lst[0]:
                b.append(lst[i])
            else:
                r.append(lst[i])
        hoar_sort(l)
        hoar_sort(r)
        n=0
        for i in l+b+r:
            lst[n]=i
            n+=1
h=[1,3,4,6,7,3,25,25,2,3443,2]
hoar_sort(h)
print(h)