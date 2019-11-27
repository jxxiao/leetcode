'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-11-27 11:53:45
@LastEditors: jxxiao
@LastEditTime: 2019-11-27 18:06:19
'''
#
# @lc app=leetcode id=93 lang=python3
#
# [93] Restore IP Addresses
#
# https://leetcode.com/problems/restore-ip-addresses/description/
#
# algorithms
# Medium (32.71%)
# Likes:    858
# Dislikes: 362
# Total Accepted:    159.8K
# Total Submissions: 484.8K
# Testcase Example:  '"25525511135"'
#
# Given a string containing only digits, restore it by returning all possible
# valid IP address combinations.
#
# Example:
#
#
# Input: "25525511135"
# Output: ["255.255.11.135", "255.255.111.35"]
#
#
#

# @lc code=start


class Solution:
    def restoreIpAddresses(self, s):
        ip = ''
        res = []
        for i in range(1, 4):
            for j in range(1, 4):
                for k in range(1, 4):
                    d = len(s) - i - j - k
                    if d > 0 and d <= 3 and i + j + k + d == len(s):
                        A = int(s[0:i])
                        B = int(s[i:i + j])
                        C = int(s[i + j:i + j + k])
                        D = int(s[i + j + k:])
                        if (A <= 255 and B <= 255 and C <= 255 and D <= 255):
                            ip = str(A)+'.'+str(B)+'.'+str(C)+'.'+str(D)
                            if len(ip) == len(s) + 3:
                                res.append(ip)
                            ip = ''
        return res


s = '25525511135'
Solution().restoreIpAddresses(s)

# @lc code=end
