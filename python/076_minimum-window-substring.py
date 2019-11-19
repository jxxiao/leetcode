#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # 统计target各个字母的字数，以及target总次数
        need, missing = collections.Counter(t), len(t)
        start, end, i = 0, 0, 0
        # index j from 1
        for j, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            if missing == 0:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                need[s[i]] += 1
                missing += 1
                if end == 0 or j - i < end - start:
                    start, end = i, j
                i += 1
        return s[start:end]


'''
s = 'ADOBECODEBANC'
t = "ABC"

Solution().minWindow(s, t)
'''

# @lc code=end
