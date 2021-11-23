class Solution:
    def balancedStringSplit(self, s: str) -> int:     
        count = 0
        stack = []
        
        top = ''
        stack.append(s[0])
        
        for i in s[1:]:
            if len(stack) == 0:
                stack.append(i)
                top = i
                
            else:
                top = stack[-1]
                
                if top == i:
                    stack.append(i)
                    
                else:
                    stack.pop()
                    if len(stack) == 0:
                        count += 1
        
        return count
      
