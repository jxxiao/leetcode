'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-04-13 21:28:06
@LastEditors: jxxiao
@LastEditTime: 2020-04-13 23:28:42
'''

#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] 分割回文串 II
#
# https://leetcode-cn.com/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (42.54%)
# Likes:    127
# Dislikes: 0
# Total Accepted:    9.6K
# Total Submissions: 22.5K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回符合要求的最少分割次数。
#
# 示例:
#
# 输入: "aab"
# 输出: 1
# 解释: 进行一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
#
#
#


# @lc code=start
class Solution:
    def minCut(self, s: str) -> int:
        size = len(s)
        if size < 2:
            return 0

        dp = [i for i in range(size)]

        for i in range(1, size):
            if self.__check_palindrome(s, 0, i):
                dp[i] = 0
                continue
            dp[i] = min([
                dp[j] + 1 for j in range(i)
                if self.__check_palindrome(s, j + 1, i)
            ])
        return dp[size - 1]

    def __check_palindrome(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True


print(Solution().minCut(""))
    # @lc code=end
