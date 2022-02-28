class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def findNeighbor(curr):
            for i in range(4):
                x = int(curr[i])
                for diff in [-1, 1]:
                    y = (x + diff + 10) % 10
                    yield curr[:i] + str(y) + curr[i+1:]
        
        
        if "0000" in deadends:
            return -1
        deadset = set(deadends)
        dq = ['0000']
        steps = 0
        
        while dq:
            for i in range(len(dq)):
                curr = dq.pop(0)
                if curr ==  target:
                    return steps

                for n in findNeighbor(curr):
                    if n in deadset:
                        continue
                    deadset.add(n)
                    dq.append(n)
            steps += 1
                
        return -1
                
