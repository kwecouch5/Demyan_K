def minPathSum(grid):
    for i in range(len(grid[0]) - 1):
        grid[0][i + 1] = grid[0][i] + grid[0][i + 1]
    for i in range(len(grid) - 1):
        grid[i + 1][0] = grid[i][0] + grid[i + 1][0]
    for i in range(len(grid) - 1):
        for j in range(len(grid[0]) - 1):
            if grid[i][j + 1] > grid[i + 1][j]:
                grid[i + 1][j + 1] = grid[i + 1][j + 1] + grid[i + 1][j]
            else:
                grid[i + 1][j + 1] = grid[i + 1][j + 1] + grid[i][j + 1]
    return grid[len(grid) - 1][len(grid[0]) - 1]