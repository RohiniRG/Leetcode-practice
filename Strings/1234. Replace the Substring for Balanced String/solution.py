class Solution:
    def isSatisfied(self, p1, p2, balanced_c, freq):        
        for i in freq:            
            if freq[i] > balanced_c:
                return False
            
        return True
  
    
    def balancedString(self, s: str) -> int:
        balanced_count = len(s) / 4
        substring_count = len(s)
        p1 = 0
        p2 = 0
        
        freq = {
            'Q': 0, 'W': 0, 'E': 0, 'R': 0
        }
        
        for i in s:
            freq[i] += 1

        while p1 <= p2 and p2 < len(s) + 1:
            if self.isSatisfied(p1, p2, balanced_count, freq):
                freq[s[p1]] += 1
                p1 += 1
                if substring_count > (p2 - p1 + 1):
                    substring_count = p2 - p1 + 1

            else:
                if p2 >= len(s):
                    return substring_count
                var = s[p2]
                freq[var] -= 1
                p2 += 1

        return substring_count   
    
