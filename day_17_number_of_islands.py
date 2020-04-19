class Solution:
    def is_valid(self, row, col, grid):
        return 0 <= row < len(grid) and 0 <= col < len(grid[0])
    def dfs(self, row, col, grid, visited):
        visited[row][col] = True
        if grid[row][col] == "0": return
        if self.is_valid(row, col + 1, grid) and not visited[row][col + 1]: self.dfs(row, col + 1, grid, visited)
        if self.is_valid(row + 1, col, grid) and not visited[row + 1][col]: self.dfs(row + 1, col, grid, visited)
        if self.is_valid(row, col - 1, grid) and not visited[row][col - 1]: self.dfs(row, col - 1, grid, visited)
        if self.is_valid(row - 1, col, grid) and not visited[row - 1][col]: self.dfs(row - 1, col, grid, visited)
    def numIslands(self, grid):
        visited = [[False for _ in row] for row in grid]
        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and not visited[row][col]:
                    num_islands += 1
                    self.dfs(row, col, grid, visited)
        return num_islands
def main():
    grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    print(Solution().numIslands(grid))
if __name__ == '__main__':
    main()


        