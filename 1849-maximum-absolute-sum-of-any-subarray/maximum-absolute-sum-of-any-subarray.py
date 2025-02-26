class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_pos = -inf
        min_cache = inf
        max_cache = -inf
        for x in nums:
            max_cache = max(0, x, x+max_cache)
            min_cache = min(0, x, x+min_cache)

            max_pos = max(max_pos, max(abs(min_cache), max_cache))
        
        return max_pos