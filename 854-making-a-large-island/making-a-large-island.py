class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        # Suppose we have a map that for each pixel contains
        # number of pixels in the same island and also island number (unique id)
        # 
        # Then the best pixel to change will maximise:
        # Sum of areas on unique neighboring islands  
        # 

        # Classes contain grid (island_id, area). The default (ocean) is (-1, 0)
        classes = [[(-1, 0) for _ in range(m)] for _  in range(n)]
        nclusters = 0

        # Visit all pixels in island and return them
        # Also, remove them from the original grid so they are skipped in the future
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

        # Set the same island_id and area for pixels belonging in the same island
        def fill(cells, value):
            for x, y in cells:
                classes[x][y] = value

        res = 0
        # Visit and map all islands
        for i in range(n):
            for j in range(m):
                # Found island, need to visit it
                if grid[i][j] == 1:
                    cluster = dfs(i, j)
                    fill(cluster, (nclusters, len(cluster)))
                    nclusters += 1
                    res = max(res, len(cluster))
        
        # Check all ocean pixels
        for i in range(n):
            for j in range(m):
                if classes[i][j][0] == -1:
                    # Adjacent islands (their id, and area)
                    connected = []
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx = i + dx
                        ny = j + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            connected.append(classes[nx][ny])
                    
                    # Need to consider only unique islands
                    # Example: in this case, pixel (o) will connect the same island
                    # 
                    # xxx
                    # x.o
                    # xxx
                    # 
                    combined_sum = 1
                    unique_classes = set()
                    for clas, num in connected:
                        if clas not in unique_classes:
                            unique_classes.add(clas)
                            combined_sum += num
                    res = max(res, combined_sum)
            
        # No islands - we can create one with area of 1
        return max(res, 1)
                

