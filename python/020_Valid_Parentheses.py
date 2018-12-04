class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        set = ['(', '{', '[']
        dict = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in set:
                stack.append(ch)
            else:
                top = stack.pop() if stack else '#'
                if dict[ch] != top:
                    return False
        if stack:
            return False
        else:
            return True
