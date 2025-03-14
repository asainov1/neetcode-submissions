class Solution:
    def rotate(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        k = k % n
        nums[:] = nums[n - k:] + nums[:n - k]


    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        arr = [i for sublist in grid for i in sublist]
        self.rotate(arr, k)
        grid = []
        for i in range(rows):
            temp = []
            for j in range(cols):
                temp.append(arr[i * cols + j])
            grid.append(temp)
        return grid
