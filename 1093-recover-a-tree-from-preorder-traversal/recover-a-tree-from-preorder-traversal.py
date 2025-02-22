# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        def tokenizer(s):
            arr = s.split('-')
            offset = -1
            for x in arr:
                if x == '':
                    offset += 1
                else:
                    yield int(x), offset+1
                    offset = 0
        
        tokens = list(tokenizer(traversal))
        print(tokens)

        def rec(level):
            if len(tokens) == 0:
                return None
            value, lvl = tokens[0]
            if lvl == level:
                tokens.pop(0)
                node = TreeNode(value)
                node.left = rec(level+1)
                node.right = rec(level+1)
                return node

            return None

        return rec(0)
        