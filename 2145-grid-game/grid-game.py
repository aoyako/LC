class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_sum = sum(grid[0])
        bot_sum = sum(grid[1])

        res = inf
        acum_top = 0
        acum_bot = bot_sum
        for i in range(len(grid[0])):
            acum_top += grid[0][i]
            acum_bot -= grid[1][i-1] if i >= 1 else 0
            res = min(res, max(top_sum-acum_top, bot_sum-acum_bot))
        
        return res


        