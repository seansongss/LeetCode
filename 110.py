from typing import Optional
import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True 
            
        def Height(node):
            if not node:
                return 0
            
            leftHeight = Height(node.left)
            rightHeight = Height(node.right)
            if leftHeight < 0 or rightHeight < 0 or abs(leftHeight - rightHeight) > 1:
                return -1
            
            return 1 + max(leftHeight, rightHeight)
        
        return Height(root) >= 0