class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans = None
        
        def findLca(root):
            if root is None:
                return 0
            
            left = findLca(root.left)
            right = findLca(root.right)
            
            curr_found = root.val == p.val or root.val == q.val
            
            if curr_found + left + right >= 2:
                self.ans = root
                
            return curr_found or left or right
        
        findLca(root)
        return self.ans
                
