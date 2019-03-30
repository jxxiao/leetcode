#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# https://leetcode.com/problems/length-of-last-word/description/
#
# algorithms
# Easy (32.14%)
# Total Accepted:    240.9K
# Total Submissions: 749.6K
# Testcase Example:  '"Hello World"'
#
# Given a string s consists of upper/lower-case alphabets and empty space
# characters ' ', return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of non-space
# characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5
#
#
#


class Solution:
    def lengthOfLastWord(self, s: 'str') -> 'int':
        return len(s.rstrip().split(' ')[-1])

