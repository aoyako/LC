class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend]
        times.sort()

        last = 0
        empty = []
        taken = []
        for come, go in times:
            while len(taken) != 0 and taken[0][0] <= come:
                _, pos = heappop(taken)
                heappush(empty, pos)
            if len(empty) == 0:
                heappush(empty, last)
                last += 1
            
            pos = heappop(empty)
            if [come, go] == target:
                return pos
            heappush(taken, (go, pos))
        
        return -1
        