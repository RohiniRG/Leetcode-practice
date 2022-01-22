# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.cam_count = 0
        covered = {None}
        
        def dfs(root, par=None):
            if root:
                dfs(root.left, root)
                dfs(root.right, root)
                
                if (par is None and root not in covered or root.left not in covered or root.right not in covered):
                    self.cam_count += 1
                    covered.update({root, par, root.left, root.right})
                    
        dfs(root, None)
        return self.cam_count
            
