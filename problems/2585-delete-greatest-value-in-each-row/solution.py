class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            grid[i] = sorted(grid[i]) 

        total_sum = 0 
        for col in range(cols):
            max_in_col = 0
            for row in range(rows):
                if grid[row]:
                    max_in_col = max(grid[row].pop(0), max_in_col)
                    
            total_sum += max_in_col 
        return (total_sum)

                
