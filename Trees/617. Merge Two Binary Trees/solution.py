# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root2 is None:
            return root1
        if root1 is None:
            return root2
        
        root2.left = self.mergeTrees(root2.left, root1.left)
        root2.right = self.mergeTrees(root2.right, root1.right)
        root2.val += root1.val
        
        return root2
        
