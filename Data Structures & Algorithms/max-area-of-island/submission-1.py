class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def fill(grid: List[List[int]], i: int, j: int) -> int:
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            return 1 + fill(grid, i + 1, j) + fill(grid, i, j + 1) + fill(grid, i - 1, j) + fill(grid, i, j - 1) 
        
        max_ = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                max_ = max(max_, fill(grid, i, j))
        return max_

# [
#     [0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
#     [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
#     [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0], 
#     [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]
# ]