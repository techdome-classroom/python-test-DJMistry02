class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        ans = 0
        row = len(grid)
        col = len(grid[0])
        vis = [[0]]
        return 0