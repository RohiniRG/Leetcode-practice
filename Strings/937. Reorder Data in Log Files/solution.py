class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def myfunc(x):
            return x[1:]
        
        letter = []
        digit = []
        for each in logs:
            each_list = each.split()
            
            if each_list[1].isalpha():
                letter.append(each_list)
            else:
                each_ = ' '.join(each_list)
                digit.append(each_)
        
        letter.sort()
        letter.sort(key=myfunc) 
        
        for i in range(len(letter)):
            each_ = ' '.join(letter[i])
            letter[i] = each_
            
        return letter+digit
                
