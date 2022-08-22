# Day 4

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        while n > 1:
            n = n/4
            
        if n == 1:
            return True
        return False

# RESULTS
# Runtime: 41 ms, faster than 77.16% of Python3 online submissions for Power of Four.
# Memory Usage: 13.9 MB, less than 54.38% of Python3 online submissions for Power of Four.
