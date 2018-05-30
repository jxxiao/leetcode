class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: return ""
        short = min(strs, key = len)
        for i, ch in enumerate(short):
            for compare in strs:
                if ch != compare[i]:
                    return short[:i]
        return short
