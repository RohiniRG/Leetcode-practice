class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        res = []
        summ = 0
        row_count = 0
        i = 0
        while (i < len(s)):
            summ += widths[ord(s[i])-97]
            
            if summ > 100:
                summ = 0
                row_count += 1
                summ += widths[ord(s[i])-97]
                
            i = i + 1
        
        return [row_count+1, summ]

