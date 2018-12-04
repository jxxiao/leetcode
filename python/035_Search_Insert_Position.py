class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for key, value in enumerate(nums):
            if value < target:
                continue
            else:
                return key
        return(len(nums))
