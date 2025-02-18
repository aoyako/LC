class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res = ''
        cache = []

        for i, c in enumerate(pattern+'I'):
            cache.append(str(i+1))

            if c == 'I':
                res += ''.join(cache[::-1])
                cache = []

        return res