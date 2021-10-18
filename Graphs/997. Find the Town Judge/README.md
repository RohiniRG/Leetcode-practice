# Question number: [997](https://leetcode.com/problems/find-the-town-judge/)

## Difficulty: Easy
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.


## Example 1:
Input: n = 3, trust = [[1,3],[2,3]]

Output: 3

## Example 2:
Input: n = 3, trust = [[1,3],[2,3],[3,1]]

Output: -1

## Constraints:

1 <= n <= 1000

0 <= trust.length <= 10<sup>4</sup>

trust[i].length == 2

All the pairs of trust are unique ai != bi

1 <= ai, bi <= n

# Submission details:

92 / 92 test cases passed.

Runtime: 736 ms

Memory Usage: 18.9 MB

