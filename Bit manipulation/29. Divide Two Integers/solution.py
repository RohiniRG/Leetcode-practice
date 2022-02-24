class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 0
        if (dividend < 0) ^ (divisor < 0):
            sign = -1

        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        
        while dividend >= divisor:
            q = 0
            while divisor << q <= dividend:
                q += 1
            dividend -= divisor << q - 1
            ans += 1 << q - 1
        
        if sign < 0:
            ans = -ans
        return min(max(-2147483648, ans), 2147483647) 

