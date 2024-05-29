from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def diameter(node, result):
            if not node:
                return 0
            
            left = diameter(node.left, result)
            right = diameter(node.right, result)

            result[0] = max(result[0], left + right)

            return 1 + max(left, right)
        
        result = [0]
        diameter(root, result)

        return result[0]