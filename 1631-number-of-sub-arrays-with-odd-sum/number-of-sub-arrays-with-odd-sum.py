class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        res = 0
        cache = 0
        even = 0
        odd = 0
        for x in arr:
            cache += x
            if cache % 2 == 0:
                even += 1
                res += odd
            else:
                odd += 1
                res += even + 1
        
        return res % (10**9 + 7)
        