class Solution:
    def minimumDeletions(self, s: str) -> int:
        a_count = 0
        b_count = 0
        for i in s:
            if i == "a":
                a_count += 1
        
        res = a_count + b_count
        for i in s:
            if i == "a":
                a_count -= 1
            else:
                b_count += 1
                
            res = min(res, a_count+b_count)
            
        return res
       
