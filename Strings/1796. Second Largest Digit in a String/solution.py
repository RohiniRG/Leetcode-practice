class Solution:
    def secondHighest(self, s: str) -> int:
        store = []
        for i in s:
            if i.isdigit():
                store.append(i)
                
        set_store = set(store)
        if len(set_store) >= 2:
            return sorted(set_store)[-2]
        else:
            return -1
        
