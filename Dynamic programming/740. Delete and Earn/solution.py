class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        x = dict()
        for i in nums:
            if i not in x.keys():
                x[i] = 1
            else:
                x[i] += 1
        
        prev = None
        avoid = using = 0
        for k in sorted(x):
            if k - 1 != prev:
                avoid, using = max(avoid, using), k * x[k] + max(avoid, using)
            else:
                avoid, using = max(avoid, using), k * x[k] + avoid
            prev = k
        return max(avoid, using)
    
