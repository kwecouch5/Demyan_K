def strStr(haystack, needle):
    n=len(haystack)
    m=len(needle)
    for i in range(n-m):
        if haystack[i:i+m]==needle:
            return i
    return -1