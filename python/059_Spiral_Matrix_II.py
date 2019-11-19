class Solution:
    def generateMatrix(self, n: int):
        A, low = [], n * n + 1
        while low > 1:
            low, high = low - len(A), low
            A = [list(range(low, high))] + list(list(seq) for seq in zip(*A[::-1]))
        return A


print(Solution().generateMatrix(3))