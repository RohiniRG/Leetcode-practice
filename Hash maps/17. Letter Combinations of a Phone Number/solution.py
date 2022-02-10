class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': ' '}
        
        if digits:
            all_combos = ['']
        else:
            all_combos = []

        for digit in digits:
            curr = []
            
            for letter in mapping[digit]:
                for combination in all_combos:
                    curr.append(combination + letter)
                    
            all_combos = curr
            
        return all_combos
        
