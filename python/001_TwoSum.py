class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        dic = dict()
        for index, value in enumerate(nums):
            difference = target - value
            if difference in dic:
                return [dic[difference], index]
            else:
                dic[value] = index

    def twoSum_2(self, nums, target):
        for num in nums:
            if target-num in nums:
                return [nums.index(num), nums.index(target-num)]
