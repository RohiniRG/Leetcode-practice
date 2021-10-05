# Question number: [942](https://leetcode.com/problems/di-string-match/)

## Difficulty: Easy

A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.


## Example 1:

Input: s = "IDID"

Output: [0,4,1,3,2]

## Example 2:

Input: s = "III"

Output: [0,1,2,3]

## Example 3:

Input: s = "DDI"

Output: [3,2,0,1]
 
## Constraints:

1 <= s.length <= 10<sup>5</sup>

s[i] is either 'I' or 'D'

## Submission details:

95 / 95 test cases passed.

Runtime: 60 ms

Memory Usage: 15.2 MB

