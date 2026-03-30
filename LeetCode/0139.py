def wordBreak(s,wordDict):
    w_s=set(wordDict)
    dp=[0]*(len(s)+1)
    dp[0]=1
    for i in range(1,len(s)+1):
        for j in range(i+1):
            if dp[j]==1 and s[j:i:] in w_s:
                dp[i]=1
                break
    return dp[len(dp)-1]
print(wordBreak("leetcode",  ["leet","code"]))