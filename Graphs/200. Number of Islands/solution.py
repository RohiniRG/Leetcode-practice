class Solution:
    def isConnectedComponent(self, grid, r, c):
        if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or grid[r][c] != '1':
            return
        grid[r][c] == "#" 

        self.isConnectedComponent(grid, r+1, c)
        self.isConnectedComponent(grid, r-1, c)
        self.isConnectedComponent(grid, r, c+1)
        self.isConnectedComponent(grid, r, c-1)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        no = 0
        if not grid: return 0
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.isConnectedComponent(grid, r, c)
                    no += 1
                    
        return no

