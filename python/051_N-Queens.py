'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-08-27 14:45:00
@LastEditors: jxxiao
@LastEditTime: 2020-04-21 00:40:11
'''
class Solution:
    def solveNQueens(self, n: int):
        res = []
        self.dfs([-1]*n, 0, [], res)
        return res

    # index means row, nums[index] means column
    def dfs(self, nums, index, path, res):
        # 遍历一遍结束，把结果加到res里
        if index == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            nums[index] = i
            # 在(index, nums[index])处放皇后
            if self.isValid(nums, index):
                tmp = '.'*len(nums)
                self.dfs(nums, index + 1, path + [tmp[:i]+'Q'+tmp[i+1:]], res)

    # 判断能否放置，因为是按行放，所以不用考虑行，只需要考虑列和对角线。
    # 列判断：遍历已经放置的nums，nums[i] == nums[n]就不行
    # 对角线判断： 判断abs(nums[i]-nums[n]) == n - i即可
    def isValid(self, nums, n):
        for i in range(n):
            if abs(nums[i]-nums[n]) == n - i or nums[i] == nums[n]:
                return False
        return True

Solution().solveNQueens(4)