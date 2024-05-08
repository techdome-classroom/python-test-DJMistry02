class Solution:
   
    def DFS(curRow, curCol, maxRow, maxCol, vis):
        dRow = [-1,1,0,0]
        dCol = [0,0,-1,1]
        for i in range(4):
            nRow = curRow + dRow[i]
            nCol = curCol + dCol[i]
            if nRow>=0 and nRow<maxRow and nCol>=0 and nCol<maxCol and 

    def getTotalIsles(self, grid: list[list[str]]) -> int:
        ans = 0
        row = len(grid)
        col = len(grid[0])
        vis = [[[0] * col] for _ in range(row)]
        
        # see vis
        print(vis)

        
        return 0