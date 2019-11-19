class Solution:
    def solveNQueens(self, n):
        self.res = 0
        self.dfs([-1]*n, 0)
        return self.res

    # index means row, nums[index] means column
    def dfs(self, nums, index):
        if index == len(nums):
            self.res += 1
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.isValid(nums, index):
                tmp = '.'*len(nums)
                self.dfs(nums, index + 1)

    def isValid(self, nums, n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True
