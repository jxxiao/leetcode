'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-03-18 23:22:23
@LastEditors: jxxiao
@LastEditTime: 2020-03-18 23:43:05
'''
#
# @lc app=leetcode.cn id=290 lang=python3
#
# [290] 单词规律
#
# https://leetcode-cn.com/problems/word-pattern/description/
#
# algorithms
# Easy (42.22%)
# Likes:    137
# Dislikes: 0
# Total Accepted:    19.2K
# Total Submissions: 45.6K
# Testcase Example:  '"abba"\n"dog cat cat dog"'
#
# 给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。
#
# 这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。
#
# 示例1:
#
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
#
# 示例 2:
#
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
#
# 示例 3:
#
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
#
# 示例 4:
#
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
#
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
#
#

# @lc code=start
class Solution:
    def wordPattern(self, pattern, str):
        res = str.split(' ')
        return list(map(pattern.index, pattern)) == list(map(res.index, res))


pattern = "abba"
str = "dog cat cat dog"

Solution().wordPattern(pattern, str)
# @lc code=end
