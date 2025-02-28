class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        @lru_cache(10000)
        def rec(i, j):
            res = 'a'*10000
            if i == len(str1):
                return str2[j:]
            if j == len(str2):
                return str1[i:]
            if str1[i] == str2[j]:
                return str2[j] + rec(i+1, j+1)

            s1 = str2[j] + rec(i, j+1)
            s2 = str1[i] + rec(i+1, j)
            if len(s1) < len(res):
                res = s1
            if len(s2) < len(res):
                res = s2

            return res
        
        return rec(0, 0)