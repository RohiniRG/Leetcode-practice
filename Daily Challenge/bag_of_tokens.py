# Day 5

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        curr_score = 0
        max_score = 0
        while len(tokens) > 0:
            min_token = min(tokens)
            if power >= min_token:
                power -= min_token
                tokens.remove(min_token)
                curr_score += 1    
            elif curr_score >= 1:
                max_token = max(tokens)
                power += max_token
                tokens.remove(max_token)
                curr_score -= 1
            else:
                break
                
            if curr_score > max_score:
                max_score = curr_score
                
        return max_score

# RESULTS:
# Runtime: 485 ms, faster than 5.19% of Python3 online submissions for Bag of Tokens.
# Memory Usage: 13.9 MB, less than 77.36% of Python3 online submissions for Bag of Tokens.
