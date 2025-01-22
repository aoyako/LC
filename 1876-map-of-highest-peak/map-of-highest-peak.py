class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])

        visited = set()
        cache = deque()
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    cache.append((i, j, 0))
                    isWater[i][j] = 0
                    visited.add((i,j))
        
        while cache:
            x, y, c = cache.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                if 0 <= x+dx < n and 0 <= y+dy < m and (x+dx,y+dy) not in visited:
                    visited.add((x+dx,y+dy))
                    isWater[x+dx][y+dy] = c+1
                    cache.append((x+dx,y+dy, c+1))
                    
        return isWater