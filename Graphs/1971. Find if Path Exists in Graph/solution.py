class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        if [start, end] in edges or [end, start] in edges:
            return True
        
        store = dict()
        for i in edges:
            # print(store)
            if i[0] not in store.keys():
                store[i[0]] = {i[1]}
            else:
                store[i[0]].add(i[1])
            if i[1] not in store.keys():
                store[i[1]] = {i[0]}
            else:
                store[i[1]].add(i[0])
                
        visited = set()
        q = [start]
        
        while len(q)>0:
            node = q.pop()
            
            if node == end: 
                return True
            
            visited.add(node)
            q.extend(n for n in store[node] if n not in visited)
            
        return False
            
 
