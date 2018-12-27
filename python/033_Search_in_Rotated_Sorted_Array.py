class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        L = 0
        R = len(nums) - 1

        while True:
            if L > R:
                return -1
            m = (L + R) // 2
            if nums[L] == target:
                return L
            if nums[R] == target:
                return R
            if nums[m] == target:
                return m

            if nums[L] < target and target < nums[m]:
                R = m - 1
                continue

            if target > nums[m] and target < nums[R]:
                L = m + 1
                continue

            if nums[L] > nums[m]:
                R = m - 1
                continue

            if nums[m] > nums[R]:
                L = m + 1
                continue

            return -1
