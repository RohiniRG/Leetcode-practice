# Question number: [904](https://leetcode.com/problems/fruit-into-baskets/)

## Difficulty: Medium
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
 
## Example 1:
Input: fruits = [1,2,1]

Output: 3

Explanation: We can pick from all 3 trees.

## Constraints:
1 <= fruits.length <= 10<sup>5</sup>

0 <= fruits[i] < fruits.length

# Submission details:

90 / 90 test cases passed.

Runtime: 1030 ms

Memory Usage: 20 MB
