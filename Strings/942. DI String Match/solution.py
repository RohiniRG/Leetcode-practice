class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        lowest = 0
        highest = len(s)
        sol = []
        
        for i in s:
            if i == 'I':
                sol.append(lowest)
                lowest += 1
            if i == 'D':
                sol.append(highest)
                highest -= 1
                
        if i == 'I':
            sol.append(lowest)
            lowest += 1
        if i == 'D':
            sol.append(highest)
            highest -= 1
            
        return sol
      
      
