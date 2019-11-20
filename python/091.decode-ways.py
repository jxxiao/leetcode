'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-11-19 22:05:19
@LastEditors: jxxiao
@LastEditTime: 2019-11-20 16:17:02
'''
#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#
# https://leetcode.com/problems/decode-ways/description/
#
# algorithms
# Medium (23.07%)
# Likes:    1850
# Dislikes: 2093
# Total Accepted:    314.5K
# Total Submissions: 1.4M
# Testcase Example:  '"12"'
#
# A message containing letters from A-Z is being encoded to numbers using the
# following mapping:
#
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
#
#
# Given a non-empty string containing only digits, determine the total number
# of ways to decode it.
#
# Example 1:
#
#
# Input: "12"
# Output: 2
# Explanation: It could be decoded as "AB" (1 2) or "L" (12).
#
#
# Example 2:
#
#
# Input: "226"
# Output: 3
# Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2
# 6).
#
#

# @lc code=start


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s.startswith('0'):
            return 0
        stack = [1, 1]
        for i in range(1, len(s)):
            # 20 10 f(n) = f(n-2)
            if s[i] == '0':
                if s[i - 1] == '0' or s[i - 1] > '2':
                    return 0
                stack.append(stack[-2])
            # 9-27 f(n) = f(n-2) + f(n-1)
            elif 9 < int(s[i - 1:i + 1]) < 27:
                stack.append(stack[-2] + stack[-1])
            # 01 - 09 or > 26
            else:
                stack.append(stack[-1])
        return stack[-1]


s = '226'
Solution().numDecodings(s)

# @lc code=end
