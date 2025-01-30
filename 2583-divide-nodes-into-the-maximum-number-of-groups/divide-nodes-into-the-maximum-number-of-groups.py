class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        eg = defaultdict(list)

        for a, b in edges:
            eg[a-1].append(b-1)
            eg[b-1].append(a-1)

        classes = defaultdict(int)

        for i in range(n):
            cache = [i]
            dist = [0] * n
            dist[i] = 1
            mx = 1
            root = i
            while cache:
                node = cache.pop(0)
                root = min(root, node)
                
                for nb in eg[node]:
                    if dist[nb] == 0:
                        dist[nb] = dist[node] + 1
                        mx = max(mx, dist[nb])
                        cache.append(nb)
                    elif abs(dist[nb] - dist[node]) != 1:
                        return -1
            classes[root] = max(classes[root], mx)
        return sum(classes.values())