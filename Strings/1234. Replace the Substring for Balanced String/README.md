# Question number: [1234](https://leetcode.com/problems/replace-the-substring-for-balanced-string/)

## Difficulty: Medium
You are given a string containing only 4 kinds of characters 'Q', 'W', 'E' and 'R'.

A string is said to be balanced if each of its characters appears n/4 times where n is the length of the string.

Return the minimum length of the substring that can be replaced with any other string of the same length to make the original string s balanced. Return 0 if the string is already balanced.

## Example 1:

Input: s = "QWER"

Output: 0

Explanation: s is already balanced.

## Example 2:

Input: s = "QQWE"

Output: 1

Explanation: We need to replace a 'Q' to 'R', so that "RQWE" (or "QRWE") is balanced.

## Example 3:

Input: s = "QQQW"

Output: 2

Explanation: We can replace the first "QQ" to "ER". 

## Constraints:

1 <= s.length <= 10<sup>5</sup>

s.length is a multiple of 4

s contains only 'Q', 'W', 'E' and 'R'.

# Submission details:

40 / 40 test cases passed.

Runtime: 280 ms

Memory Usage: 14.9 MB

