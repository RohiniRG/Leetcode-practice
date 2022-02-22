class Solution:
    def isConnectedComponent(self, grid, r, c, visited):
        if not (r < len(grid) and 0 <= r) or not (c < len(grid[0]) and 0 <= c): 
            return False
        if grid[r][c] == "0": 
            return False
        if [r, c] in visited: 
            return False
        
        visited.append([r, c])
        
        self.isConnectedComponent(grid, r+1, c, visited)
        self.isConnectedComponent(grid, r-1, c, visited)
        self.isConnectedComponent(grid, r, c-1, visited)
        self.isConnectedComponent(grid, r, c+1, visited)

        return True

    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        no = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                val = self.isConnectedComponent(grid, r, c, visited)
                if val:
                    no += 1
                    
        return no

