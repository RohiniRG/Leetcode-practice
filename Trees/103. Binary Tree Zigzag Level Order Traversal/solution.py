class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        stk1 = []        
        if root is not None:
            stk1.append(root)
        else:
            return []
        stk2 = []
        op  = []
        toggle = False
        temp = []

        while len(stk1) != 0:
            top = stk1.pop()
            temp.append(top.val)
            if not toggle:
                if top.left is not None:
                    stk2.append(top.left)
                if top.right is not None:
                    stk2.append(top.right)
            else:
                if top.right is not None:
                    stk2.append(top.right)
                if top.left is not None:
                    stk2.append(top.left)
                
            if len(stk1) == 0:
                stk1, stk2 = stk2, stk1
                toggle = not toggle
                op.append(temp)
                temp = []
                
                
        return op
        
