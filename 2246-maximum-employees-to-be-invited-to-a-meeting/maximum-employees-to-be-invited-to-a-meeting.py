class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        ins = [0]*n
        trim = [0]*n
        for i, j in enumerate(favorite):
            ins[j] += 1
        tails = [i for i, j in enumerate(ins) if not j]

        while tails:
            next = []
            for i in tails:
                temp = favorite[i]
                trim[temp] = trim[i] + 1
                ins[temp] -= 1
                if not ins[temp]:
                    next.append(temp)
            tails = next

        curone = [i for i, j in enumerate(ins) if j]
        double = 0
        loop = 0
        for i in curone:
            if ins[i] != 0:
                temp = favorite[i]
                if favorite[temp] == i:
                    double += trim[i] + trim[temp] + 2
                    ins[i] = ins[temp] = 0
                else:
                    cnt = 1
                    ins[i] = 0
                    while temp != i:
                        ins[temp] = 0
                        temp = favorite[temp]
                        cnt += 1
                    loop = max(loop, cnt)
        
        return max(loop, double)