# Question number: [1014](https://leetcode.com/problems/best-sightseeing-pair/)

## Difficulty: Medium
You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

Return the maximum score of a pair of sightseeing spots.

## Example 1:
Input: values = [8,1,5,2,6]

Output: 11

Explanation: i = 0, j = 2, values[i] + values[j] + i - j = 8 + 5 + 0 - 2 = 11

## Constraints:
2 <= values.length <= 5 * 10<sup>4</sup>

1 <= values[i] <= 1000

# Submission details:

53 / 53 test cases passed.

Runtime: 624 ms

Memory Usage: 19.9 MB

