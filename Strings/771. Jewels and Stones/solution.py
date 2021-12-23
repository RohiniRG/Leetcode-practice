class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        j_count = 0
        
        for j in jewels:
            j_count += stones.count(j)
        
        return j_count

