class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                dp[i] = nums[i]
            elif i ==1:
                dp[i] = max(nums[0], nums[1])
            else:
                dp[i] = max(dp[i-1],dp[i-2]+nums[i])
        return dp[-1]