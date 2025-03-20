def razvorot_rec(s):
    if len(s)==1:
        return s[0]
    else:
        return razvorot_rec(s[1::])+s[0]
print(razvorot_rec('abcde'))