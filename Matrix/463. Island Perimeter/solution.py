class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        peri = 0
        
        for row in range(r):
            for col in range(c):
                if grid[row][col]:
                    peri += 4
                    if row > 0:
                        peri -= grid[row-1][col]
                    if row < r-1:
                        peri -= grid[row+1][col]
                    if col > 0:
                        peri -= grid[row][col-1]
                    if col < c-1:
                        peri -= grid[row][col+1]
                        
        return peri
                    
