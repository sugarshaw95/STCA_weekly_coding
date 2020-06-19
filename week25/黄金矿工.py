class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m=len(grid)
        if m==0:
            return 0
        n=len(grid[0])
        if n==0:
            return 0
        visited=[[False for i in range(n)] for j in range(m)]
        ret=0
        def dfs(x,y,visited,summ):
            nonlocal ret
            dxs=[-1,1,0,0]
            dys=[0,0,-1,1]
            summ+=grid[x][y]
            if summ>ret:
                ret=summ
            
            for dx,dy in zip(dxs,dys):
                if 0<=x+dx<m and 0<=y+dy<n and grid[x+dx][y+dy]>0 and not visited[x+dx][y+dy]:
                    visited[x][y]=True
                    dfs(x+dx,y+dy,visited,summ)
                    visited[x][y]=False
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i,j,visited,0)
        return ret