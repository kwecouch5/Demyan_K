a=int(input())
x=int(input())
b=int(input())
y=int(input())
p=int(input())
counter=0
while a<b:
    a+=x*(p/100)
    b+=y*(p/100)
    counter+=1
print(counter)