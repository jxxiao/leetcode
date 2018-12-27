class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right, n = 0, len(nums) - 1, len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                left = right = mid
                while left > 0 and nums[left - 1] == nums[left]:
                    left -= 1
                while right + 1 < n and nums[right + 1] == nums[right]:
                    right += 1
                return [left, right]
        return [-1, -1]
