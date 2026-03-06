def gridChallenge(grid):
    sorted_grid = ["".join(sorted(row)) for row in grid]
    for col in range(len(sorted_grid[0])):
        for row in range(len(sorted_grid) - 1):
            if sorted_grid[row][col] > sorted_grid[row+1][col]:
                return "NO"
    return "YES"