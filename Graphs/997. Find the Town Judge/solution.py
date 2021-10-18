class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        array = [0]*n
        
        for a, b in trust:
            array[a-1] -= 1
            array[b-1] += 1
        
        if max(array) == n-1:
            return array.index(n-1)+1
        
        return -1
                
