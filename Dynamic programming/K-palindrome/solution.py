class Solution:
    def kPalindrome(self, str, n, k):
        # code here
        def lcs(str, revStr, m, n):
            if m==0 or n==0:
                return 0
            if str[m-1] == revStr[n-1]:
                return 1 + lcs(str, revStr, m-1, n-1)
            return max(lcs(str, revStr, m, n-1), lcs(str, revStr, m-1, n)) 
        
        n = len(str)
        if n - lcs(str, str[::-1], n, n) <= k:
            return 1
            
        return 0

