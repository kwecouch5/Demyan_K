def one_roman_lether(a):
    one_roman_lethers={}
    one_roman_lethers['M']=1000
    one_roman_lethers['D']=500
    one_roman_lethers['C']=100
    one_roman_lethers['L']=50
    one_roman_lethers['X']=10
    one_roman_lethers['V']=5
    one_roman_lethers['I']=1
    return one_roman_lethers[a]


def romanToInt(s):
    result=0
    for i in range(len(s)-1):
        if one_roman_lether(s[i])>=one_roman_lether(s[i+1]):
            result+=one_roman_lether(s[i])
        else:
            result+=-one_roman_lether(s[i])
    result+=one_roman_lether(s[len(s)-1])
    return result
print(romanToInt(""))



