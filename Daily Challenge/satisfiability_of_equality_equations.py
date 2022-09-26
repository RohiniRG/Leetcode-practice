# Day 9

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}
        
        def find(x):
            if x not in parent:
                return x
            else:
                return find(parent[x])
            
        for i in equations:
            if i[1]=="=":
                a = i[0]
                b = i[-1]
                x = find(a)
                y = find(b)
                if x!=y:
                    parent[y] = x
                    
        for i in equations:
            if i[1]=="!" and find(i[0])==find(i[-1]):
                return False
        return True

# RESULTS:
# Runtime: 102 ms, faster than 15.20% of Python3 online submissions for Satisfiability of Equality Equations.
# Memory Usage: 14 MB, less than 69.95% of Python3 online submissions for Satisfiability of Equality Equations.
