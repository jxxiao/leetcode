class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        new_s = '#'.join('${}#'.format(s))
        length = len(new_s)
        P = [0] * length

        c = r = 0
        for i in range(1, length-1):
            P[i] = (i < r) and min(P[2*c - i], r - i)

            while new_s[i + 1 + P[i]] == new_s[i - 1 - P[i]]:
                P[i] += 1

            if i + P[i] > r:
                c, r = i, i + P[i]

        maxLen, centerIndex = max((length, i) for i, length in enumerate(P))
        return s[(centerIndex - maxLen)//2:(centerIndex + maxLen)//2]
