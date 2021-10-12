class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        num = [0 for i in range(len(strs[0]))]
        
        for i in range(len(strs)-1):
            for j in range(len(strs[i])):
                if strs[i][j] > strs[i+1][j]:
                    num[j] += 1
        delete = 0
        for i in num:
            if i > 0:
                delete += 1
        return delete
      
