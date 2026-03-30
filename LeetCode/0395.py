def longestSubstring(s,k):
    m=0
    for i in range(len(s)):
        d = dict()
        for j in range(len(s)):
            if j>=i:
                if s[j] not in d:
                    d[s[j]]=1
                else:
                    d[s[j]]+=1
            o=1
            su=0
            for j in d.values():
                if j>=k:
                    o=1
                    su+=j
                else:
                    o=0
                    break
            if o==1:
                if su>m:
                    m=su
    return m
print(longestSubstring('bbaaacbd',3))