def min_simple(n):
    while True:
        delit=2
        n+=1
        if n%delit!=0:
            while 2 ** 0.5 * n < delit:
                delit += 1
                if n % delit==0:
                    break
            return n
print(min_simple(115))