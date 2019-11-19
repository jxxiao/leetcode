import math


class Solution:
    # 递归
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        else:
            return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)

    # space O（m*n）
    def uniquePathsDP(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j - 1][i] + dp[j][i - 1]
        return dp[m - 1][n - 1]
        print(dp)

    def uniquePathsFAC(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // (
            math.factorial(m - 1) * math.factorial(n - 1))

    def uniquePathsFAC2(self, m: int, n: int) -> int:
        k = m + n - 1 - 1
        l = n - 1 if n - 1 < m - 1 else m - 1
        num = 1
        den = 1
        while l > 0:
            num *= k
            den *= l
            k -= 1
            l -= 1
        return num//den


print(Solution().uniquePathsFAC(3, 2))
