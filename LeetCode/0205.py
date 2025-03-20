def isIsomorphic(s,t):
    if len(s)!=len(t):
        return False
    dict_1={}
    dict_2={}
    j=0
    for i in range(len(s)):
        if s[i] in dict_1:
            if dict_1[s[i]]!=t[j]:
                return False
        dict_1[s[i]]=t[j]
        j+=1
    j=0
    for i in range(len(t)):
        if t[i] in dict_2:
            if dict_2[t[i]]!=s[j]:
                return False
        dict_2[t[i]]=s[j]
        j+=1
    return True
print(isIsomorphic('eggl','peeh'))