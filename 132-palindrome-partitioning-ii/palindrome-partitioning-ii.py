class Solution:
    def minCut(self, s: str) -> int:
        @lru_cache(None)
        def is_poly(b, e):
            if b == e or b + 1 == e:
                return True
            return s[b] == s[e-1] and is_poly(b+1, e-1)
        
        @lru_cache(None)
        def rec(b):
            if b == len(s):
                return -1
            res = inf
            for e in range(len(s), b, -1):
                if is_poly(b, e):
                    l = rec(e)
                    res = min(res, 1+l)
            
            return res
        
        return rec(0)
        