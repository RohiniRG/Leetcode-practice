# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def checkCurrent(root1, root2):
            if root1 is None or root2 is None:
                return root1 == root2

            return (root1.val==root2.val 
                    and checkCurrent(root1.left, root2.left)
                    and checkCurrent(root1.right, root2.right))
                    
        
        if root is None:
            return False

        return (self.isSubtree(root.left, subRoot) or 
                self.isSubtree(root.right, subRoot) or
                checkCurrent(root, subRoot))
