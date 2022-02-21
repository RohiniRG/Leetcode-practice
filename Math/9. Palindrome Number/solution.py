class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        og = x
        reversed = 0
        while x != 0:
            curr = x % 10
            reversed = reversed * 10 + curr
            x = x // 10
            
        return reversed == og
        
