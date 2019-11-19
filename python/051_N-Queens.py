class Solution:
    def solveNQueens(self, n: int):
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res

    # index means row, nums[index] means column
    def dfs(self, nums, index, path, res):
        if index == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            if self.isValid(nums, index):
                tmp = '.'*len(nums)
                self.dfs(nums, index + 1, path + [tmp[:i]+'Q'+tmp[i+1:]], res)

    def isValid(self, nums, n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True
