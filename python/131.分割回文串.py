'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-04-12 12:52:54
@LastEditors: jxxiao
@LastEditTime: 2020-04-19 18:06:58
'''
#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] 分割回文串
#
# https://leetcode-cn.com/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (66.17%)
# Likes:    258
# Dislikes: 0
# Total Accepted:    27.8K
# Total Submissions: 41.7K
# Testcase Example:  '"aab"'
#
# 给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。
#
# 返回 s 所有可能的分割方案。
#
# 示例:
#
# 输入: "aab"
# 输出:
# [
# ⁠ ["aa","b"],
# ⁠ ["a","a","b"]
# ]
#
#

# @lc code=start


class Solution:
    def partition(self, s: str):

        def backtracking(s, start, length, path, res):
            if start == length:
                res.insert(-1, path[:])
                return
            for i in range(start, length):
                # 判断起点到i是不是回文，不是的话i++
                if not checkPalindrome(s, start, i):
                    continue
                '''
                path.append(s[start:i+1])
                backtracking(s, i + 1, length, path, res)
                path.pop()
                '''
                backtracking(s, i + 1, length, path.append(s[start:i+1]), res)



        def checkPalindrome(s, left, right):
            while left < right:
                if s[left] is not s[right]:
                    return False
                left += 1
                right -= 1
            return True
        path = []
        res = []
        backtracking(s, 0, len(s), path, res)
        return res


Solution().partition("aab")

# @lc code=end
