# Day 6

class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        n = len(data)

        i = 0
        while i < n:
            if data[i] < 128: 
                k = 1
            elif 192 <= data[i] < 224: 
                k = 2
            elif 224 <= data[i] < 240: 
                k = 3
            elif 240 <= data[i] < 248:
                k = 4
            else:
                return False
            if n - i < k:
                return False
            else:
                for j in range(i + 1, i + k):
                    if not 128 <= data[j] < 192:
                        return False
            i += k

        return True

# RESULTS:
# Runtime: 152 ms, faster than 73.83% of Python3 online submissions for UTF-8 Validation.
# Memory Usage: 14.2 MB, less than 70.76% of Python3 online submissions for UTF-8 Validation.
