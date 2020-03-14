'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-02-25 22:54:25
@LastEditors: jxxiao
@LastEditTime: 2020-02-28 20:18:33
'''
#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (34.04%)
# Likes:    902
# Dislikes: 2495
# Total Accepted:    488.4K
# Total Submissions: 1.4M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#

# @lc code=start


class Solution:
    def isPalindrome(self, s: str) -> bool:
        letters = 'qwertyuiopasdfghjklzxcvbnm'
        numbers = '1234567890'

        s = s.lower()
        s_new = ''

        for x in s:
            if x in letters or x in numbers:
                s_new += x
        if s_new == "":
            return True
        half = int(((len(s_new)-1))/2)
        if s_new == "":
            return True
        for i in range(0, half+1):
            if s_new[i] == s_new[len(s_new) - 1 - i]:
                continue
            else:
                return False
        return True

# @lc code=end
