fin=9999999999999999999999999999999999999999999
for n in range(601,700):
    h=0
    nn=bin(n)[2::]
    if n%2==0:
        nn='10'+nn+'0'
    else:
        nn=nn+bin(nn.count('1'))[2::]
    print(fin)