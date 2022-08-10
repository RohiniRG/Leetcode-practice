# Day 3

import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getBST(self, start, end, nums):
        if start == end:
            return TreeNode(nums[start])
        
        if start > end:
            return None
        
        mid = math.ceil((start+end)/2)
        print(mid)
        root = TreeNode(nums[mid])
        root.left = self.getBST(start, mid-1, nums)
        root.right = self.getBST(mid+1, end, nums)
        return root
        
        
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.getBST(0, len(nums)-1, nums)

# RESULTS:
# Runtime: 109 ms, faster than 76.06% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.
# Memory Usage: 15.7 MB, less than 32.22% of Python3 online submissions for Convert Sorted Array to Binary Search Tree.

