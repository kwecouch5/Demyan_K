def minCut(s):
    counter=0
    s_0=0
    for i in range(1,len(s)+1):
        print(s[s_0:i:])
        print(s[s_0:i:][::-1])
        if s[s_0:i:]!=s[s_0:i:][::-1]:
            
            print(0)
            s_0=i
    return counter
print(minCut('abba'))
