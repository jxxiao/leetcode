
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        r = re.match(r"[-+]?\d+", str.lstrip())
        return 0 if r == None else -2**31 if int(r.group(0))<-2**31 else 2**31-1 if int(r.group(0))>2**31-1 else int(r.group(0))   