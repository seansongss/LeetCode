# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:        
        def isGood(node, maxParentVal):
            if not node:
                return 0
            
            if node.val < maxParentVal:
                return isGood(node.left, maxParentVal) + isGood(node.right, maxParentVal)
            else:
                return 1 + isGood(node.left, node.val) + isGood(node.right, node.val)
            
        return 1 + isGood(root.left, root.val) + isGood(root.right, root.val)