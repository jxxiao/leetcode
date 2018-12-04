class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 1
        for num in nums:
            if num == res:
                res += 1
        return res
