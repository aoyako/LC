class Solution:
    def check(self, nums: List[int]) -> bool:
        broken = False
        prev = -inf
        for x in nums:
            if x < prev:
                if broken:
                    return False
                broken = True
            prev = x
        
        return nums[-1] <= nums[0] if broken else True
        