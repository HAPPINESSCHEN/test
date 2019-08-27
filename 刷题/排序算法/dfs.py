def surfaceArea(grid):
    n = len(grid)
    ans = 0
    grid += [[0] * n]
    for i in range(n):
        grid[i] += [0]
        for j in range(n):
            ans += grid[i][j] * 4 - 2 * (min(grid[i][j], grid[i + 1][j]) + min(grid[i][j], grid[i][j + 1])) + 2 if \
            grid[i][j] > 0 else 0
    return ans

grid=[[2,2],[2,1],[1,1]]
print(surfaceArea(grid))