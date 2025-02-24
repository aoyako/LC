class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(edges)+1
        eg = defaultdict(list)
        for u, v in edges:
            eg[u].append(v)
            eg[v].append(u)

        parent = [-1]*n
        bob_moves = [inf]*n 

        def rec(i, p):
            parent[i] = p
            for j in eg[i]:
                if j == p:
                    continue
                rec(j, i)

        rec(0, -1)

        x = bob
        move = 0
        while x != -1:
            bob_moves[x] = move
            move += 1
            x = parent[x]

        def rec_sum(i, dist, prev):
            alice = 0
            if dist < bob_moves[i]:
                alice = amount[i]
            elif dist == bob_moves[i]:
                alice = amount[i]//2

            end = True
            ss = -inf

            for j in eg[i]:
                if j == prev: continue
                end = False
                ss = max(ss, rec_sum(j, dist+1, i))

            return alice if end else alice + ss

        return rec_sum(0, 0, -1)
    
        