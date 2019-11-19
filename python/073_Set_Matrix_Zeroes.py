class Solution:
    def setZeroes(self, matrix) -> None:
        raw_zreos = set()
        column_zeros = set()

        for i, nums in enumerate(matrix):
            for j, n in enumerate(nums):
                if n == 0:
                    raw_zreos.add(i)
                    column_zeros.add(j)
        for i, nums in enumerate(matrix):
            for j, _ in enumerate(nums):
                if i in raw_zreos or j in column_zeros:
                    matrix[i][j] = 0


matrix = [[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]]

Solution().setZeroes(matrix)
