    def DFS(curRow, curCol, maxRow, maxCol, vis, grid):
        vis[curRow][curCol] = 1
        dRow = [-1,1,0,0]
        dCol = [0,0,-1,1]
        for i in range(4):
            nRow = curRow + dRow[i]
            nCol = curCol + dCol[i]
            if nRow>=0 and nRow<maxRow and nCol>=0 and nCol<maxCol and grid[nRow][nCol] == 'L' and vis[nRow][nCol] == 0:
                Solution.DFS(nRow,nCol,maxRow,maxCol,vis,grid)
        return

    def getTotalIsles(self, grid: list[list[str]]) -> int:
        ans = 0
        row = len(grid)
        col = len(grid[0])
        vis = [[[0] * col] for _ in range(row)]
        
        # see vis
        print(vis)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 'L' and vis[i][j] == 0:
                    ans += 1
                    Solution.DFS(i,j,row,col,vis,grid)
        return ans