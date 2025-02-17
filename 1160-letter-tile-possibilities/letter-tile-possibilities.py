class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def rec(cache):
            ss = 0
            for k, v in cache.items():
                if v > 0:
                    nextcache = cache.copy()
                    nextcache[k] -= 1
                    ss += 1 + rec(nextcache)
            return ss
        
        cache = Counter(tiles)
        return rec(cache)
        