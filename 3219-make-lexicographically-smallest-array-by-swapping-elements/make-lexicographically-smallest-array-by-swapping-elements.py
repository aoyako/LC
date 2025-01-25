class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        cache = sorted(nums)
        clusters = []

        curr_cluster = []
        for x in cache:
            if len(curr_cluster) == 0 or x- curr_cluster[-1] <= limit:
                curr_cluster.append(x)
            else:
                clusters.append(((curr_cluster[0], curr_cluster[-1]), curr_cluster))
                curr_cluster = [x]
        clusters.append(((curr_cluster[0], curr_cluster[-1]), curr_cluster))

        res = []
        for x in nums:
            pos = bisect_right(clusters, x, key=lambda x: x[0][0])
            (lower, upper), cluster = clusters[pos-1]
            # for (lower, upper), cluster in clusters:
                # if len(cluster) != 0 and lower <= x and x <= upper:
            print(lower, upper)
            res.append(cluster[0])
            cluster.pop(0)

        return res

        