# Question number: [232](https://leetcode.com/problems/implement-queue-using-stacks/)

## Difficulty: Easy
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

- void push(int x) Pushes element x to the back of the queue.
- int pop() Removes the element from the front of the queue and returns it.
- int peek() Returns the element at the front of the queue.
- boolean empty() Returns true if the queue is empty, false otherwise.

## Example 1:
Input: ["MyQueue", "push", "push", "peek", "pop", "empty"] [[], [1], [2], [], [], []]

Output: [null, null, null, 1, 1, false]

Explanation:

MyQueue myQueue = new MyQueue();

myQueue.push(1); // queue is: [1]

myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)

myQueue.peek(); // return 1

myQueue.pop(); // return 1, queue is [2]

myQueue.empty(); // return false

## Constraints:
1 <= x <= 9

At most 100 calls will be made to push, pop, peek, and empty.

All the calls to pop and peek are valid.

# Submission details:
22 / 22 test cases passed.

Runtime: 38 ms

Memory Usage: 13.9 MB

