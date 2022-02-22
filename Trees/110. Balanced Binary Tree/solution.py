class Solution:
    bal = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def maxHt(root):
            if root is None:
                return 0
            
            left_ht = maxHt(root.left)
            right_ht = maxHt(root.right)
            
            if abs(left_ht-right_ht) <= 1 and self.bal: 
                self.bal = True
            else: 
                self.bal = False
            
            return 1 + max(left_ht, right_ht)
        
        maxHt(root)
        return self.bal

