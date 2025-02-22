# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        # Iterate over string to find node value and depth (level)
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

        def reconstruct(level):
            if len(tokens) == 0:
                return None
            # Peek first token
            value, lvl = tokens[0]
            # It is on the same level, so construct a new node
            if lvl == level:
                # Token is used here
                tokens.pop(0)
                node = TreeNode(value)
                # Don't care if reconstruct fails for children, it will return None (no children)
                node.left = reconstruct(level+1)
                node.right = reconstruct(level+1)
                return node

            return None

        return reconstruct(0)
        