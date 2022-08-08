# Day 2

class Solution:
    memo = dict()
    def getLIS(self, subarr):
        if len(subarr) == 1:
            self.memo[subarr[0]] = 1
            return self.memo[subarr[0]]
        
        largest = 1
        for k, v in self.memo.items():
            curr_count = 1
            if k > subarr[0]:
                curr_count += v
                if curr_count > largest:
                    largest = curr_count
                    
        self.memo[subarr[0]] = largest
        return self.memo[subarr[0]]
            

    def lengthOfLIS(self, nums: List[int]) -> int:
        self.memo = dict()
        largest = 1
        for ind in range(len(nums)-1, -1, -1):
            curr_largest = self.getLIS(nums[ind:])
            if curr_largest > largest:
                largest = curr_largest
            
        return largest

# RESULTS:
# Runtime: 1455 ms, faster than 71.15% of Python3 online submissions for Longest Increasing Subsequence.
# Memory Usage: 14.5 MB, less than 5.65% of Python3 online submissions for Longest Increasing Subsequence.

