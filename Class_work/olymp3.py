n=int(input())
a=[]
x=0
y=0
for i in range(n):
    c=int(input())
    b=int(input())
    a.append(c)
    a.append(b)
for i in range(0,len(a)-1,2):
    x+=a[i]
for i in range(1,len(a),2):
    y+=a[i]
x=x/n
y=y/n
m_1=0
m_2=0
for i in range(0,len(a)-1,2):
    if abs(a[i]-x)>m_1:
        m_1=abs(a[i]-x)
for i in range(1,len(a)-1,2):
    if abs(a[i]-y)>m_2:
        m_2=abs(a[i]-y)
print(max(m_2,m_1))
