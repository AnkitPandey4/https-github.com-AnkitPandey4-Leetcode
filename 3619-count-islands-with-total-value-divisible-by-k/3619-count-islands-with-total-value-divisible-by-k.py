class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r: int, c: int) -> int:
            island_sum = grid[r][c]
            grid[r][c] = 0 
            
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] > 0:
                    island_sum += dfs(nr, nc)
            return island_sum

        for i in range(m):
            for j in range(n):
                if grid[i][j] > 0:
                    if dfs(i, j) % k == 0:
                        island_count += 1
                        
        return island_count
