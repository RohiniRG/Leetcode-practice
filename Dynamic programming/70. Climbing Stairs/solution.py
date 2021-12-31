class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        step1 = 1
        step2 = 2
        
        for i in range(3, n+1):
            steps = step1 + step2
            step1 = step2
            step2 = steps
            
        return step2

