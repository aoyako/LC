class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        cache = defaultdict(int)
        for a in nums:
            for b in nums:
                if a != b:
                    cache[a*b] += 1
        
        res = 0
        for _, v in cache.items():
            res += (v//2-1)*v//2*4

        
        return res
        