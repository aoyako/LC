class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        rows = [0]*n
        cols = [0]*m

        for i in range(n):
            for j in range(m):
                rows[i] += grid[i][j]
                cols[j] += grid[i][j]
        
        res = 0
        for i in range(n):
            for j in range(m):
                res += grid[i][j]*(1 if rows[i]+cols[j] != 2 else 0)
        
        return res
        