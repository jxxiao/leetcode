'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-11-27 21:35:36
@LastEditors: jxxiao
@LastEditTime: 2019-11-27 21:57:46
'''
#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (29.21%)
# Likes:    1016
# Dislikes: 58
# Total Accepted:    128.9K
# Total Submissions: 436.9K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#
#


# @lc code=start
class Solution:
    def isInterleave(self, s1, s2, s3):
        if len(s1) + len(s2) != len(s3):
            return False
        last = set([(0, 0)])
        for c in s3:
            current = set()
            for i, j in last:
                if i < len(s1) and s1[i] == c:
                    current.add((i+1, j))
                if j < len(s2) and s2[j] == c:
                    current.add((i, j+1))
            if not current:
                return False
            last = current
        return True


s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"

Solution().isInterleave(s1, s2, s3)
# @lc code=end
