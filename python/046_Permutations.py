class Solution:
    def permute(self, nums):
        res = []
        self.DFS(nums, [], res)
        return res

    def DFS(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.DFS(nums[:i]+nums[i+1:], path+[nums[i]], res)


nums = [1, 2, 3]
print(Solution().permute(nums))
