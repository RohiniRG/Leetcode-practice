class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon = {
            'b': 0,
            'a': 0,
            'l': 0,
            'o': 0,
            'n': 0
        }
        
        for i in text:
            if i in balloon.keys():
                balloon[i] += 1
                
        return min(
                    balloon['a'], balloon['b'], balloon['n'],
                    balloon['l']//2, balloon['o']//2
                )

      
