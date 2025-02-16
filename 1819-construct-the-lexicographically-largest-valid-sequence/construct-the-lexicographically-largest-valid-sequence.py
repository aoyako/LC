class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        arr = [None]*(2*n-1)
        visited = set()

        def rec(idx):
            if len(visited) == n:
                return True
            if idx >= len(arr):
                return False
            if not arr[idx] is None:
                return rec(idx+1)

            for num in range(n-1, -1, -1):
                if num in visited:
                    continue
                
                if num == 0:
                    visited.add(num)
                    arr[idx] = 1
                    if rec(idx+1):
                        return True
                    visited.remove(num)
                    arr[idx] = None
                    return False

                if idx + num + 1 >= len(arr):
                    return False
                if not arr[idx + num + 1] is None:
                    continue

                arr[idx] = num + 1  
                arr[idx + num + 1] = num + 1
                visited.add(num)
                if rec(idx + 1):
                    return True
                visited.remove(num)
                arr[idx + num + 1] = None
            arr[idx] = None
            return False

        rec(0)
        return arr