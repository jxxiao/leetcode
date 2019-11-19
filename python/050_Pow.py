class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        for i in range(n):
            res = res * x
        return res

    def myPow2(self, x: float, n: int) -> float:
        if n == 0: return 1
        if n < 0: return 1/self.myPow2(x, -n)
        res = self.myPow2(x, n // 2)
        if n % 2 == 0:
            return res * res
        else:
            return res * res * x


print(Solution().myPow(5, 0))
