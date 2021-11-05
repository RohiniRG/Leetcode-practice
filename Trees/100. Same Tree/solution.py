# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        t1_q = []
        t2_q = []
        
        root_ind = 0
        t1_q.append(p)
        t2_q.append(q)
        comp = []
        
        while len(t1_q) > 0 and len(t2_q) > 0:
            node1 = t1_q.pop(0)
            node2 = t2_q.pop(0)
            
            if node1.val != node2.val:
                return False
            
            if node1.left and node2.left:
                t1_q.append(node1.left)
                t2_q.append(node2.left)
            elif node1.left or node2.left:
                return False
            
            if node1.right and node2.right:
                t1_q.append(node1.right)
                t2_q.append(node2.right)
            elif node1.right or node2.right:
                return False
            
        return True

