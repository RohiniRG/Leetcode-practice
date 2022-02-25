class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        types = {}
        start_win_i = 0
        max_len = 0
        
        for max_win_i in range(len(fruits)):
            if fruits[max_win_i] not in types:
                types[fruits[max_win_i]] = 1
            else:
                types[fruits[max_win_i]] += 1
                
            while len(types) > 2:
                types[fruits[start_win_i]] -= 1
                if not types[fruits[start_win_i]]:
                    types.pop(fruits[start_win_i])
                start_win_i += 1
            max_len = max(max_len, max_win_i-start_win_i+1)
        
        return max_len

