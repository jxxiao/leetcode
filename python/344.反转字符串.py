'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-04-19 15:17:53
@LastEditors: jxxiao
@LastEditTime: 2020-04-19 15:45:59
'''

#
# @lc app=leetcode.cn id=344 lang=python3
#
# [344] 反转字符串
#
# https://leetcode-cn.com/problems/reverse-string/description/
#
# algorithms
# Easy (69.40%)
# Likes:    233
# Dislikes: 0
# Total Accepted:    130.3K
# Total Submissions: 186.4K
# Testcase Example:  '["h","e","l","l","o"]'
#
# 编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。
#
# 不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。
#
# 你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。
#
#
#
# 示例 1：
#
# 输入：["h","e","l","l","o"]
# 输出：["o","l","l","e","h"]
#
#
# 示例 2：
#
# 输入：["H","a","n","n","a","h"]
# 输出：["h","a","n","n","a","H"]
#
#


# @lc code=start
class Solution:
    def reverseString(self, s):
        """
        Do not return anything, modify s in-place instead.
        """

        for i in range(len(s) // 2):
            s[i], s[~i] = s[~i], s[i]

# @lc code=end
