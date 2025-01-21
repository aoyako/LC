class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        top_sum = sum(grid[0])
        bot_sum = sum(grid[1])

        # .  .  .  i  .  .
        # x  x  x  x  a4 a5  | total sum = top_sum
        # b1 b2 b3 x  x  x   | total sum = bot_sum
        # 
        # What the second player can get?
        # SECOND_SCORE = max [left on top (a(i+1), ..., an), left on bottom (b0, ... b(i-1))]
        # 
        # First player wants to minimize this sum:
        # min across (i=0,n) SECOND_SCORE(i)

        res = inf
        acum_top = 0
        acum_bot = bot_sum
        for i in range(len(grid[0])):
            acum_top += grid[0][i]
            acum_bot -= grid[1][i-1] if i >= 1 else 0
            res = min(res, max(top_sum-acum_top, bot_sum-acum_bot))
        
        return res


        