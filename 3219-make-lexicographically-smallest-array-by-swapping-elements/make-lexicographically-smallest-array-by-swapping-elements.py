class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        cache = sorted(nums)

        # Each cluster is characterized by the lower and upper bound and its elements
        # Elements in single cluster can be swapped between each other freely
        # For example, if limit=1, one possible clusters are [1, 2, 3], [5, 6], [8]
        clusters = []

        curr_cluster = []
        for x in cache:
            if len(curr_cluster) == 0 or x- curr_cluster[-1] <= limit:
                curr_cluster.append(x)
            else:
                # (lower_bound, upper_bound, elements)
                clusters.append(((curr_cluster[0], curr_cluster[-1]), curr_cluster))
                curr_cluster = [x]
        clusters.append(((curr_cluster[0], curr_cluster[-1]), curr_cluster))

        res = []
        for x in nums:
            # Find element's cluster and replace it with the smallest in the
            # corresponding cluster
            pos = bisect_right(clusters, x, key=lambda x: x[0][0])
            (lower, upper), cluster = clusters[pos-1]
            res.append(cluster[0])
            cluster.pop(0)

        return res

        