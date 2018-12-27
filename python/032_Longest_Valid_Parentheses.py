class Solution:
    def longestValidParentheses(self, s):
        dp = [0] * (len(s) + 1)
        for i, c in enumerate(s):
            if c == ')' and i - 1 - dp[i] >= 0 and s[i - 1 - dp[i]] == '(':
                dp[i + 1] = 2 + dp[i] + dp[i - dp[i] - 1]
        return max(dp)


s = ")()())"
result = Solution().longestValidParentheses(s)
print(result)
