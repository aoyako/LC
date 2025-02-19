class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = [] 

        def rec(s):
            if len(s) == n:
                res.append(s)
                return
            
            for c in ['a', 'b', 'c']:
                if not s or s[-1] != c:
                    rec(s + c)
        
        rec('')
        res.sort()
        return res[k - 1] if k <= len(res) else ''