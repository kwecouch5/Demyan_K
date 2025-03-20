def merge(l,r):
    s=[0]*(len(l)+len(r))
    i_l=0
    i_r=0
    i_s=0
    while i_l<len(l) and i_r<len(r):
        if l[i_l] >= r[i_r]:
            s[i_s]=r[i_r]
            i_r += 1
            i_s+=1
        else:
            s[i_s]=l[i_l]
            i_l += 1
            i_s+=1
    while i_l<len(l):
        s[i_s]=l[i_l]
        i_s+=1
        i_l+=1
    while i_r<len(r):
        s[i_s]=r[i_r]
        i_s+=1
        i_r+=1
    return s


def merge_sort(s):
    if len(s)<=1:
        return s
    else:
        l=len(s)//2
        return merge(merge_sort(s[:l:]),merge_sort(s[l::]))


def merge_sort_1(s):
    if len(s)<=1:
        return
    else:
        l=len(s)//2
        s_1=merge_sort_1(s[:l:])
        s_2=merge_sort_1(s[l::])
        final=merge(s_1, s_2)
        for i in range(len(s)):
            s[i]=final[i]
            return s
a=[2,6,1,4,3,9,5,8,7,0,10]
merge_sort_1(a)
print(a)
