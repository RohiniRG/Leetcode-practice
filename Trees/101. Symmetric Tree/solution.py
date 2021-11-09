# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:    
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recursion(branch_1, branch_2):
            if branch_1 is None or branch_2 is None:
                return branch_1 == branch_2
            if branch_1.val != branch_2.val:
                return False 
            return recursion(branch_1.right, branch_2.left) and         recursion(branch_1.left, branch_2.right)
        return recursion(root.left, root.right)

