class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        
        f0 = 0
        f1 = 1
        f2 = 1
        
        for i in range(3, n+1):
            trib = f0 + f1 + f2
            f0 = f1
            f1 = f2
            f2 = trib
            
        return f2

