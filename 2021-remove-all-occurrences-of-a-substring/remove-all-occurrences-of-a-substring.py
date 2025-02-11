class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        cache = []
        for c in s:
            cache.append(c)
            if len(cache) >= len(part) and ''.join(cache[-len(part):]) == part:
                cache = cache[:-len(part)]

        return ''.join(cache)
        