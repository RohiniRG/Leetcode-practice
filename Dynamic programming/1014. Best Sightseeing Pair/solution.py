class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        imax = values[0] + 0
        bestscore = -1
        
        for i in range(1, len(values)):
            bestscore = max(imax + values[i] - i, bestscore)
            imax = max(imax, values[i] + i)
            
        
        return bestscore
    
