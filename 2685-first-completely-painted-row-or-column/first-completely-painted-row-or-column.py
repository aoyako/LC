class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        order = [0]*len(arr)
        for i, x in enumerate(arr):
            order[x-1] = i
        
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            for j in range(m):
                mat[i][j] = order[mat[i][j]-1]
        
        mn = inf
        for i in range(n):
            mx = 0
            for j in range(m):
                mx = max(mx, mat[i][j])
            mn = min(mn, mx)
        for j in range(m):
            mx = 0
            for i in range(n):
                mx = max(mx, mat[i][j])
            mn = min(mn, mx)

        return mn
            
        