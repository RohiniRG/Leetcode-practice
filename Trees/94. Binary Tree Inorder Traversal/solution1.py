# RECURSIVE approach

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    res = []
    
    def inorderUtil(self, root, res):
        if root == None:
            return
        
        if root.left != None:
            self.inorderUtil(root.left, res)
        res.append(root.val)    
        if root.right != None:
            self.inorderUtil(root.right, res)
        
        # return res
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.inorderUtil(root, res)
        
        return res
      
