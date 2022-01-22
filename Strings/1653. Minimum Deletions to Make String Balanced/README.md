# Question number: [1653](https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/)

## Difficulty: Medium
You are given a string s consisting only of characters 'a' and 'b'.

You can delete any number of characters in s to make s balanced. s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

## Example 1:
Input: s = "aababbab"

Output: 2

Explanation: You can either:
Delete the characters at 0-indexed positions 2 and 6 ("aababbab" -> "aaabbb"), or
Delete the characters at 0-indexed positions 3 and 6 ("aababbab" -> "aabbbb").

## Constraints:
1 <= s.length <= 10<sup>5</sup>

s[i] is 'a' or 'b'.

# Submission details:

157 / 157 test cases passed.

Runtime: 1110 ms

Memory Usage: 15 MB
