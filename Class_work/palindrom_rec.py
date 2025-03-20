def is_palindrom(s):
    if len(s)==0 or len(s)==1:
        return True
    else:
        s[0]==s[-1] and is_palindrom(s[1:-1:])
print(is_palindrom('ifkfi'))