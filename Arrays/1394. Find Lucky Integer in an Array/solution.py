class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = dict()
        
        for i in arr:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
        
        max_k = -1
        for k, v in freq.items():
            # print(k, v)
            if k == v and k > max_k:
                max_k = k
                
        return max_k
            
