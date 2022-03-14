class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Solution array which will store the products
        res = [1 for i in range(len(nums))]
        
        # Current element for res = prefix product * suffix product
        preprod = 1
        sufprod = 1
        
        for i in range(len(nums)):
            # Storing the prefix product
            res[i] *= preprod
            # Updating the prefix product
            preprod *= nums[i]
            
            # Storign the suffix product
            res[-i-1] *= sufprod
            # Updating the suffix product
            sufprod *= nums[-1-i]
            
        return res

    
