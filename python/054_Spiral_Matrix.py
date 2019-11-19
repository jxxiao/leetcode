class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res = res + matrix.pop(0)
            matrix = list(list(i) for i in zip(*matrix))[::-1]
        return res


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().spiralOrder(matrix))
