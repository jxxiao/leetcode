class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return
        l, h = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0 for _ in range(l)] for _ in range(h)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, h):
            dp[i][0] = dp[i - 1][0] * (1 - obstacleGrid[i][0])
        for i in range(1, l):
            dp[0][i] = dp[0][i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, h):
            for j in range(1, l):
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) * (
                    1 - obstacleGrid[i][j])
        return dp[-1][-1]

    # space O(n)
    def uniquePathsWithObstacles2(self, obstacleGrid):
        if not obstacleGrid:
            return
        l, h = len(obstacleGrid[0]), len(obstacleGrid)
        cur = [0] * l
        cur[0] = 1 - obstacleGrid[0][0]
        for i in range(1, l):
            cur[i] = cur[i - 1] * (1 - obstacleGrid[0][i])
        for i in range(1, h):
            cur[0] *= 1 - obstacleGrid[i][0]
            for j in range(1, l):
                cur[j] = (cur[j - 1] + cur[j]) * (1 - obstacleGrid[i][j])
        return cur[-1]

    def uniquePathsWithObstacles3(self, obstacleGrid):
        if not obstacleGrid:
            return
        l, h = len(obstacleGrid[0]), len(obstacleGrid)
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for i in range(1, h):
            obstacleGrid[i][0] = obstacleGrid[i - 1][0] * (
                1 - obstacleGrid[i][0])
        for i in range(1, l):
            obstacleGrid[0][i] = obstacleGrid[0][i - 1] * (
                1 - obstacleGrid[0][i])
        for i in range(1, h):
            for j in range(1, l):
                obstacleGrid[i][j] = (
                    obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]) * (
                        1 - obstacleGrid[i][j])
        return obstacleGrid[-1][-1]


nums = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]

print(Solution().uniquePathsWithObstacles3(nums))
