class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        prev = nums[0]
        mx = 1
        cs = 1
        cb = 1
        for x in nums[1:]:
            if x > prev:
                cs += 1
                mx = max(mx, cs, cb)
                cb = 1
            elif x < prev:
                cb += 1
                mx = max(mx, cs, cb)
                cs = 1
            else:
                mx = max(mx, cs, cb)
                cs = 1
                cb = 1
            prev = x
        
        return mx
        
        