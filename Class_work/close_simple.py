def is_simple(n):
    i=2
    while i*i<n:
        if n%i==0:
            return False
        else:
            i+=1
    return True
def closer_simple(n):
    n_0=n
    m=n
    n+=1
    while True:
        if is_simple(n):
            s_b=n
            break
        else:
            n+=1
    while m>1:
        if is_simple(m):
            break
        else:
            m+=-1
    if n_0-m>=s_b-n_0:
        return m
    else:
        return s_b
print(closer_simple(2))