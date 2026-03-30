def coinChange(coins,amount):
    c=[0]*(amount+1)
    c[0]=0
    l=-1
    for i in range(len(coins)):
        if coins[i]<amount:
            c[coins[i]]=1
    for i in range(1,len(c)):
        if c[i]==0:
            for j in range(len(coins)):
                if coins[j]<=i:
                    if c[i-coins[j]]+1<l or l==-1:
                        l=c[i-coins[j]]+1

            c[i]=l
            l=-1
    print(c)
    if c[amount]==0:
        return -1
    else:
        return c[amount]
print(coinChange([1],0))