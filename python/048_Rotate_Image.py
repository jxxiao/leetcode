class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[:] = map(list, zip(*matrix[::-1]))
        return matrix


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(Solution().rotate(matrix))
