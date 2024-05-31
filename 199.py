from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def Traversal(node, h):
            if node:
                if len(res) == h:
                    res.append(node.val)
                Traversal(node.right, h + 1)
                Traversal(node.left, h + 1)

        Traversal(root, 0)
        return res