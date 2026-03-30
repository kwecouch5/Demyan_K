def longestPalindrome(s):
    n=''
    for i in range(len(s)):
        for j in range(len(s)):
            if j>=i:
                if s[i:j+1:]==s[:j+1:-1]:
                    if len(s[i:j+1:])>len(n):
                        n=s[i:j+1:]
    return n
print(longestPalindrome('babad'))