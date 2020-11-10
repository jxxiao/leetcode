'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2018-12-17 21:19:33
@LastEditors: jxxiao
@LastEditTime: 2020-04-17 22:51:26
'''
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        new_s = '#'.join('${}#'.format(s))
        length = len(new_s)
        P = [0] * length

        c = mx = 0
        for i in range(1, length-1):
            P[i] = (i < mx) and min(P[2*c - i], mx - i)

            while new_s[i + 1 + P[i]] == new_s[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > mx:
                c, mx = i, i + P[i]

        maxLen, centerIndex = max((length, i) for i, length in enumerate(P))
        return s[(centerIndex - maxLen)//2:(centerIndex + maxLen)//2]

    def isPalindrome(self, s):
        for i in range(len(s)//2):
            if s[i] != s[len(s)-i-1]:
                return False
        return True

    # 1. 暴力破解
    def bruteForce(self, s):
        res = ""
        maxlen = 0
        for start in range(len(s)-1):
            for end in range(start+1, len(s)):
                subString = s[start:end+1]
                if self.isPalindrome(subString) and len(subString) > maxlen:
                    res = subString
                    maxlen = len(subString)
        return res

    # 2.优化破解 p(i,j) = p(i+1, j-1) && s[i]==s[j]
    def bruteForce_2(self, s):
        maxlen = 0
        P = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(1, len(s)+1):
            for start in range(len(s)):
                end = start + i - 1
                if end >= len(s):
                    break
                P[start][end] = (i == 1 or i == 2 or P[start+1][end-1]) and s[start]==s[end]
                if (P[start][end]) and i > maxlen:
                    maxPal = s[start:end+1]
        return maxPal

    def manacher(self, s):
        # 消灭奇偶
        new_s = '#'.join('${}#'.format(s))



a = 'abbahopxpo'

print(Solution().longestPalindrome(a))