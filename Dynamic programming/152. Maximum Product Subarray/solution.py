def maxProduct(self, nums: List[int]) -> int:
        
        max_prod = max(nums)
        
        # Maintain max and min pointer
        currMax, currMin = 1, 1
        
        for i in nums:
            if i == 0:
                currMax, currMin = 1, 1
                continue
            
            temp = currMax*i
            currMax = max(currMax*i, currMin * i, i)
            currMin = min(temp, currMin * i, i)
            
            max_prod = max(currMax, max_prod)
                
        return max_prod
      
