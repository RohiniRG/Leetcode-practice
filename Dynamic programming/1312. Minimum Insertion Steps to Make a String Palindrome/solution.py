class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0]*(n+1) for _ in range(n+1)]
        
        for i in range(n-1, -1, -1):
            for j in range(n):
                if i < j:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1]
                    else:
                        dp[i][j] = 1+ min(dp[i+1][j], dp[i][j-1])
        return dp[0][n-1]
    
