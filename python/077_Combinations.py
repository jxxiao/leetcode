class Solution:
    def combine(self, n: int, k: int):
        com = [[]]
        for _ in range(k):
            com = [[i] + c for c in com for i in range(1, c[0] if c else n + 1)]
        return com


Solution().combine(4, 2)
