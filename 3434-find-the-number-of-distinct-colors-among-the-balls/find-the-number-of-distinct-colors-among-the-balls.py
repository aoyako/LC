class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        cache = defaultdict(set)
        colors = {}

        res = []
        for i, c in queries:
            if i in colors:
                old_c = colors[i]
                cache[old_c].remove(i)
                if len(cache[old_c]) == 0:
                    del cache[old_c]
            colors[i] = c
            cache[c].add(i)

            res.append(len(cache))
        
        return res