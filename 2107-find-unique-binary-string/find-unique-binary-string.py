class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def to_num(s):
            return sum([int(x)<<i for i,x in enumerate(s)])
        def from_num(x, l):
            res = ""
            for i in range(l):
                res += str(x%2)
                x //= 2
            return res
        
        cache = set([])  
        for x in nums:
            cache.add(to_num(x))
        for i in range(0, 1<<len(nums[0])+1):
            if i not in cache:
                return from_num(i, len(nums[0]))
        
        return from_num(0, len(nums[0]))
        