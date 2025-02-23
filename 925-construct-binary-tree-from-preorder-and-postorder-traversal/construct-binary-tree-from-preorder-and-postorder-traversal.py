# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        postorder = [TreeNode(x) for x in postorder]
        cache = []
        for x in postorder:
            if not cache or preorder.index(cache[-1].val) < preorder.index(x.val):
                cache.append(x)
            else:
                right = cache.pop(-1)
                left = None if len(cache) == 0 or preorder.index(cache[-1].val) < preorder.index(x.val) else cache.pop(-1)
                
                x.left = left
                x.right = right
                cache.append(x)
        
        return cache[0]


        