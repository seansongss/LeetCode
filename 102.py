from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        trees = {0: [root]}
        res = []
        h = 0

        while (trees):
            tmp_lst = []
            if not trees[h]:
                break
            trees[h+1]=[]
            while trees[h]:
                tmp = trees[h].pop(0)
                if tmp:
                    tmp_lst.append(tmp.val)
                    trees[h+1].append(tmp.left)
                    trees[h+1].append(tmp.right)
            if tmp_lst:
                res.append(tmp_lst)
            h += 1
        return res
    
print(Solution().levelOrder(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
