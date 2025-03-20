from itertools import count


def lengthOfLastWord(s):
    s=s[::-1]
    summ=0
    count=1
    for i in range(len(s)):
        if s[i]==' ' and summ==0:
            None
        elif s[i]==' ':
            return summ
        elif len(s)==count:
            return summ+1
        else:
            summ+=1
        count+=1
print(lengthOfLastWord('dfsssf '))
