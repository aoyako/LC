class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        classes = list(range(len(edges) + 1))

        def find_class(node):
            if classes[node] != node:
                classes[node] = find_class(classes[node])
            return classes[node]

        for a, b in edges: 
            ca, cb = find_class(a), find_class(b)

            if ca == cb:
                return [a, b]
 
            classes[ca] = cb
        
        return [-1, -1]