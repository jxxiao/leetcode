#
# @lc app=leetcode id=89 lang=python3
#
# [89] Gray Code
#
# https://leetcode.com/problems/gray-code/description/
#
# algorithms
# Medium (46.99%)
# Likes:    478
# Dislikes: 1341
# Total Accepted:    146.5K
# Total Submissions: 310.8K
# Testcase Example:  '2'
#
# The gray code is a binary numeral system where two successive values differ
# in only one bit.
#
# Given a non-negative integer n representing the total number of bits in the
# code, print the sequence of gray code. A gray code sequence must begin with
# 0.
#
# Example 1:
#
#
# Input: 2
# Output: [0,1,3,2]
# Explanation:
# 00 - 0
# 01 - 1
# 11 - 3
# 10 - 2
#
# For a given n, a gray code sequence may not be uniquely defined.
# For example, [0,2,3,1] is also a valid gray code sequence.
#
# 00 - 0
# 10 - 2
# 11 - 3
# 01 - 1
#
#
# Example 2:
#
#
# Input: 0
# Output: [0]
# Explanation: We define the gray code sequence to begin with 0.
# A gray code sequence of n has size = 2^n, which for n = 0 the size is 2^0 =
# 1.
# Therefore, for n = 0 the gray code sequence is [0].
#
#
#


# @lc code=start
class Solution:
    def grayCode(self, n):
        nums = []
        for i in range(1 << n):
            nums.append(i ^ i >> 1)
        return nums


print(Solution().grayCode(2))
# @lc code=end
