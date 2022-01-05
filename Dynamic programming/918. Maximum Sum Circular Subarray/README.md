# Question number: [918](https://leetcode.com/problems/maximum-sum-circular-subarray/)

## Difficulty: Medium
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

## Example 1:
Input: nums = [5,-3,5]

Output: 10

Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.

## Constraints:
n == nums.length

1 <= n <= 3 * 10<sup>4</sup>

-3 * 10<sup>4</sup> <= nums[i] <= 3 * 10<sup>4</sup>

# Submission details:

111 / 111 test cases passed.

Runtime: 720 ms

Memory Usage: 18.6 MB
