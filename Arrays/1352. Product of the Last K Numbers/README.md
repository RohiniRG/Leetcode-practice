# Question number: [1352](https://leetcode.com/problems/product-of-the-last-k-numbers/)

## Difficulty: Medium
Design an algorithm that accepts a stream of integers and retrieves the product of the last k integers of the stream.

Implement the ProductOfNumbers class:

ProductOfNumbers() Initializes the object with an empty stream.
void add(int num) Appends the integer num to the stream.
int getProduct(int k) Returns the product of the last k numbers in the current list. You can assume that always the current list has at least k numbers.
The test cases are generated so that, at any time, the product of any contiguous sequence of numbers will fit into a single 32-bit integer without overflowing.

 
## Example 1:
Input: 
["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]

[[],[3],[0],[2],[5],[4],[2],[3],[4],[8],[2]]

Output: 
[null,null,null,null,null,null,20,40,0,null,32]

## Constraints:
0 <= num <= 100

1 <= k <= 4 * 10<sup>4</sup>

# Submission details:

33 / 33 test cases passed.

Runtime: 276 ms

Memory Usage: 31.3 MB
