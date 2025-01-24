class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        visited = set()

        @lru_cache(None)
        def is_save(node):
            if len(graph[node]) == 0:
                return True

            visited.add(node)
            for nb in graph[node]:
                if nb in visited:
                    return False
                elif not is_save(nb):
                    return False

            visited.remove(node)
            return True

        return sorted([x for x in range(len(graph)) if is_save(x)])