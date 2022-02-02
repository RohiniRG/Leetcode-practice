class Solution:
    max_path = float('-inf')
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def updateMaxPathSum(root):
            if root is None:
                return 0
            
            sum_left = max(updateMaxPathSum(root.left), 0)
            sum_right = max(updateMaxPathSum(root.right), 0)
            
            curr_sum = root.val + sum_left + sum_right
            
            self.max_path = max(curr_sum, self.max_path)
            
            return root.val + max(sum_left, sum_right)
        
        updateMaxPathSum(root)
        return self.max_path
            
