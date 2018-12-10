class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        # 判断dividend和divisor符号是否相同，
        
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1

        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

dividend, divisor = 10, 3
Solution().divide(dividend, divisor)
