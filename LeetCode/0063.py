def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    dp = [0] * n
    dp[0] = 1
    print(dp)

    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j]:
                dp[j] = 0
            elif j > 0:
                dp[j] += dp[j - 1]
                print(dp)

    return dp[n - 1]
print(uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]]))