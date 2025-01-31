class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        classes = [[(-1, 0) for _ in range(m)] for _  in range(n)]
        nclusters = 0

        def dfs(x, y):
            cache = [(x, y)]
            visited = []
            grid[x][y] = 0
            while cache:
                x, y = cache.pop()
                visited.append((x, y))
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                        grid[nx][ny] = 0
                        cache.append((nx, ny))
            return visited

        def fill(cells, value):
            for x, y in cells:
                classes[x][y] = value

        res = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cluster = dfs(i, j)
                    fill(cluster, (nclusters, len(cluster)))
                    nclusters += 1
                    res = max(res, len(cluster))
        
        for i in range(n):
            for j in range(m):
                if classes[i][j][0] == -1: 
                    connected = []
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx = i + dx
                        ny = j + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            connected.append(classes[nx][ny])
                    
                    combined_sum = 1
                    unique_classes = set()
                    for clas, num in connected:
                        if clas not in unique_classes:
                            unique_classes.add(clas)
                            combined_sum += num
                    res = max(res, combined_sum)
            
        
        return max(res, 1)
                

