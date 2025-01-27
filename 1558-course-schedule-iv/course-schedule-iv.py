class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        eg = defaultdict(list)
        for a, b in prerequisites:
            eg[a].append(b)
        
        def path(b, e):
            cache = [b]
            visited = set([b])
            while cache:
                node = cache.pop()
                if node == e:
                    return True
                for nb in eg[node]:
                    if nb not in visited:
                        cache.append(nb)
                        visited.add(nb)
            return False

        res = []
        for u, v in queries:
            res.append(path(u, v))
        
        return res

        