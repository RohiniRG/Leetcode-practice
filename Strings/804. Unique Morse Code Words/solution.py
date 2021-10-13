class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ref = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = []
        for i in words:
            each = ''
            for letter in i:
                ind = ord(letter)-97
                each += ref[ind]
            
            res.append(each)
                
        return len(set(res))
			
