class Solution:
    def nextSparse (ob, n):
        # code here 
        store = []
        for i in range(n):
            store.append(n & 1)
            n >>= 1
            
        last_changed = 0
        for i in range(1, len(store)-1):
            if store[i-1] == 1 and store[i] == 1 and store[i+1] != 1:
                store[i+1] = 1
                
                for j in range(i, last_changed-1, -1):
                    store[j] = 0
                
                last_changed = i+1
                
        ans = 0
        for i in range(len(store)):
            ans += store[i] * (1 << i)
            
        return ans
      
