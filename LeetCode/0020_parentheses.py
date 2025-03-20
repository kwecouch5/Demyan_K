def isValid(s):
    lst=[]
    open=['(','[','{']
    close=[')',']','}']
    for i in range(len(s)):
        if s[i] in open:
            lst.append(open.index(s[i]))
            print(lst)
        elif s[i] in close:
            if lst and lst[-1]==close.index(s[i]):
                lst.pop()
            else:
                return False
    return not lst

print(isValid('{([d])wklrjl}'))