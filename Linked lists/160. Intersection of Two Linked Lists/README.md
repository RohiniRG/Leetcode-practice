# Question number: [160](https://leetcode.com/problems/intersection-of-two-linked-lists/)

## Difficulty: Easy
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

## Example 1:
Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3

Output: Intersected at '8'

Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.

## Example 2:
Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1

Output: Intersected at '2'

Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

## Constraints:
The number of nodes of listA is in the m.

The number of nodes of listB is in the n.

1 <= m, n <= 3 * 10<sup>4</sup>

1 <= Node.val <= 10<sup>5</sup>

0 <= skipA < m

0 <= skipB < n

intersectVal is 0 if listA and listB do not intersect.

intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.

# Submission details:
39 / 39 test cases passed.

Status: Accepted

Runtime: 246 ms

Memory Usage: 29.5 MB
