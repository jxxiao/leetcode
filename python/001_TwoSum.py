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
