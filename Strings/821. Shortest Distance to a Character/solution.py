class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        shortestDist = []
        
        prev = len(s) + 1
        for i in range(len(s)):
            if s[i] == c:
                prev = i
            if prev == len(s) + 1:
                shortestDist.append(len(s) + 1)
            else:
                shortestDist.append(abs(prev-i))
                
        prev = len(s) + 1
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                prev = i
            if prev != len(s) + 1:
                shortestDist[i] = min(abs(prev-i), shortestDist[i])
                
        return shortestDist
      
      
 
