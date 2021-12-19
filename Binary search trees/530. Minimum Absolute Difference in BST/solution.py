class Solution:        
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:        
        stack = []
        curr = root
        min_diff = 10000000
        prev = None
        while True:
            if curr is not None:
                stack.append(curr)
                curr = curr.left
            elif stack:
                curr = stack.pop()
                if prev is None:
                    prev = curr.val
                else:
                    diff = curr.val - prev
                    if diff < min_diff:
                        min_diff = diff
                    prev = curr.val
                curr = curr.right
            else:
                break    
                
            
        return min_diff
    
