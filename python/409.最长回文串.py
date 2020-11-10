'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-03-19 00:24:15
@LastEditors: jxxiao
@LastEditTime: 2020-03-19 00:26:55
'''
#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#
# https://leetcode-cn.com/problems/longest-palindrome/description/
#
# algorithms
# Easy (52.35%)
# Likes:    110
# Dislikes: 0
# Total Accepted:    18K
# Total Submissions: 34.3K
# Testcase Example:  '"abccccdd"'
#
# 给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。
#
# 在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。
#
# 注意:
# 假设字符串的长度不会超过 1010。
#
# 示例 1:
#
#
# 输入:
# "abccccdd"
#
# 输出:
# 7
#
# 解释:
# 我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
#
#
#

# @lc code=start
from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter, odd = Counter(s), 0
        for v in counter.values():
            if v % 2 == 1:
                odd += 1
        return len(s) - max(odd - 1, 0)

# @lc code=end
