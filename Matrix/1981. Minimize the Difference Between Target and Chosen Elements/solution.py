class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        R, C = len(mat), len(mat[0])
        
        S = set(mat[0])
        for r in range(1, R):
            NS = set()
            for x in set(mat[r]):
                for y in S:
                    NS.add(x + y)
            S = NS
        
        return min(abs(x - target) for x in S)

