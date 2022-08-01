class Solution:
    def uniquePaths(self, m: int, n: int, memo=dict()) -> int:
        key_1 = f'{m}, {n}'
        key_2 = f'{n}, {m}'
        
        if key_1 in memo:
            return memo[key_1]
        if key_2 in memo:
            return memo[key_2]

        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0
        
        total = self.uniquePaths(m-1, n, memo) + self.uniquePaths(m, n-1, memo)
        memo[key_1] = total
        memo[key_2] = total
        
        return memo[key_1]
        
