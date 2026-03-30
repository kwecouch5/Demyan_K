a=open('2626.txt')
n,m,k=map(int,a.readline().split())
cols={}
for _ in range(n):
    row,place=map(int,a.readline().split())
    if place not in cols:
        cols[place]=[]
    cols[place].append(row)
m=0
n_row=0
for place in cols:
    rows=sorted(cols[place])
    for i in range(1,len(rows)):
        current=rows[i]-rows[i-1]-1
        if current>0:
            if current>m:
                m=current
                n_row=rows[i]
            elif current==m:
                n_row=min(n_row,rows[i])
print(m,n_row)

