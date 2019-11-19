#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (37.59%)
# Total Accepted:    269.2K
# Total Submissions: 716.3K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
#
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
#
#
# Input: a = "1010", b = "1011"
# Output: "10101"
#
#


class Solution:
    def addBinary1(self, a: 'str', b: 'str') -> 'str':
        return bin(int(a, 2) + int(b, 2))[2:]

    def addBinary(self, a: 'str', b: 'str') -> 'str':
        res, carry = '', 0
        i, j = len(a)-1, len(b) - 1
        while i >= 0 or j >= 0 or carry:
            curval = (i >= 0 and a[i] == '1') + (j >= 0 and a[j] == '1')
            carry, rem = divmod(curval + carry, 2)
            res = 'rem' + res
            i -= 1
            j -= 1
