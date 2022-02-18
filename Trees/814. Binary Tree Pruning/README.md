# Question number: [814](https://leetcode.com/problems/binary-tree-pruning/)

## Difficulty: Medium
Given the root of a binary tree, return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

A subtree of a node node is node plus every node that is a descendant of node.

## Example 1:
Input: root = [1,null,0,0,1]

Output: [1,null,0,null,1]

Explanation: 
Only the red nodes satisfy the property "every subtree not containing a 1".
The diagram on the right represents the answer.

## Constraints:

The number of nodes in the tree is in the range [1, 200].

Node.val is either 0 or 1.

# Submission details:

30 / 30 test cases passed.

Runtime: 29 ms

Memory Usage: 13.9 MB

