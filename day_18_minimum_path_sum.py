class Solution:
    def min_sum(self, grid, row, col, dp):
        if len(grid) <= row or len(grid[0]) <= col: return float("inf")
        if dp[row][col] != None: return dp[row][col]
        if len(grid) - 1 == row and len(grid[0]) - 1 == col: return grid[row][col]
        dp[row][col] = grid[row][col] + min(self.min_sum(grid, row + 1, col, dp),\
                            self.min_sum(grid, row, col + 1, dp))
        return dp[row][col]
    def minPathSum(self, grid):
        dp = [[None for _ in grid[0]] for _ in grid]
        return self.min_sum(grid, 0, 0, dp)

def main():
    grid = [
      [1,3,1],
      [1,5,1],
      [4,2,1]
    ]
    print(Solution().minPathSum(grid))

if __name__ == '__main__':
    main()
