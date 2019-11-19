class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        n = len(matrix[0])
        l, r = 0, len(matrix)*n

        while l < r:
            mid = (l+r) // 2
            num = matrix[mid // n][mid % n]
            if num < target:
                l = mid + 1
            elif num > target:
                r = mid
            else:
                return True
        return False

matrix = [[]]
Solution().searchMatrix(matrix, 10)