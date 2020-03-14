'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-02-18 17:12:49
@LastEditors  : jxxiao
@LastEditTime : 2020-02-18 18:07:36
'''
#
# @lc app=leetcode id=115 lang=python3
#
# [115] Distinct Subsequences
#
# https://leetcode.com/problems/distinct-subsequences/description/
#
# algorithms
# Hard (36.01%)
# Likes:    953
# Dislikes: 48
# Total Accepted:    123.4K
# Total Submissions: 335.8K
# Testcase Example:  '"rabbbit"\n"rabbit"'
#
# Given a string S and a string T, count the number of distinct subsequences of
# S which equals T.
#
# A subsequence of a string is a new string which is formed from the original
# string by deleting some (can be none) of the characters without disturbing
# the relative positions of the remaining characters. (ie, "ACE" is a
# subsequence of "ABCDE" while "AEC" is not).
#
# Example 1:
#
#
# Input: S = "rabbbit", T = "rabbit"
# Output: 3
# Explanation:
#
# As shown below, there are 3 ways you can generate "rabbit" from S.
# (The caret symbol ^ means the chosen letters)
#
# rabbbit
# ^^^^ ^^
# rabbbit
# ^^ ^^^^
# rabbbit
# ^^^ ^^^
#
#
# Example 2:
#
#
# Input: S = "babgbag", T = "bag"
# Output: 5
# Explanation:
#
# As shown below, there are 5 ways you can generate "bag" from S.
# (The caret symbol ^ means the chosen letters)
#
# babgbag
# ^^ ^
# babgbag
# ^^    ^
# babgbag
# ^    ^^
# babgbag
# ⁠ ^  ^^
# babgbag
# ⁠   ^^^
#
#
#

# @lc code=start


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if not t or not s:
            return 0
        dp = [[0 for i in range(len(s) + 1)] for j in range(len(t) + 1)]
        for i in range(len(t) + 1):
            dp[i][0] = 0
        for i in range(len(s) + 1):
            dp[0][i] = 1
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if s[j-1] == t[i-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[len(t)][len(s)]


s = "rabbbit"
t = "rabbit"

Solution().numDistinct(s, t)
# @lc code=end
