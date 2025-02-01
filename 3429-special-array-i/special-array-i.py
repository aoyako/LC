class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        a = nums[0]
        for x in nums[1:]:
            if a % 2 == x % 2:
                return False
            a = x
        
        return True
        