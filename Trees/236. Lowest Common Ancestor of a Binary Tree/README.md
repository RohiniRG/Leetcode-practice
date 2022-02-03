# Question number: [236](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## Difficulty: Medium
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

## Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1

Output: 3

Explanation: The LCA of nodes 5 and 1 is 3.

## Example 2:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4

Output: 5

Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

## Constraints:

The number of nodes in the tree is in the range [2, 105].

-10<sup>9</sup> <= Node.val <= 10<sup>9</sup>

All Node.val are unique and p != q

# Submission details:
31 / 31 test cases passed.

Runtime: 122 ms

Memory Usage: 26.3 MB

