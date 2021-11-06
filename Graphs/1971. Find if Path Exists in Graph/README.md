# Question number: [1971](https://leetcode.com/problems/find-if-path-exists-in-graph/)

## Difficulty: Easy
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex start to vertex end.

Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.

## Example 1:

Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2

Output: true

Explanation: There are two paths from vertex 0 to vertex 2:

- 0 → 1 → 2, 
- 0 → 2

## Example 2:

Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5

Output: false

Explanation: There is no path from vertex 0 to vertex 5.

## Constraints:

1 <= n <= 2 * 10<sup>5</sup>

0 <= edges.length <= 2 * 10<sup>5</sup>

edges[i].length == 2

0 <= ui, vi <= n - 1 ui != vi

0 <= start, end <= n - 1

There are no duplicate edges.
There are no self edges.

# Submission details:

25 / 25 test cases passed.

Runtime: 1512 ms

Memory Usage: 104.9 MB

