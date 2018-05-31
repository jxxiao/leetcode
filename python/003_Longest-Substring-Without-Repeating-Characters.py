class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {}
        start = 0
        ans = 0

        for i, c in enumerate(s):
            if c in d:
                start = max(start, d[c] + 1)
            d[c] = i
            ans = max(ans, i - start + 1)

        return ans
