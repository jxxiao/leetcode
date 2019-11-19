class Solution:
    def minPathSum(self, grid) -> int:
        h, l = len(grid), len(grid[0])
        dp = [0] * l
        dp[0] = grid[0][0]
        for i in range(1, l):
            dp[i] = dp[i-1] + grid[0][i]
        for i in range(1, h):
            dp[0] = dp[0] + grid[i][0]
            for j in range(1, l):
                dp[j] = min(dp[j-1], dp[j]) + grid[i][j]
        return dp[-1]


nums = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]

print(Solution().minPathSum(nums))
