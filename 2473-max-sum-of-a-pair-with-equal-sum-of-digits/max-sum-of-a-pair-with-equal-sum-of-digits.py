class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_dig(x):
            return sum([int(x) for x in str(x)])
        cache = {}
        res = -1
        for x in nums:
            ss = sum_dig(x)
            if ss in cache:
                num = cache[ss]
                res = max(res, num+x)
                x = max(num, x)
            cache[ss] = x
        
        return res
        