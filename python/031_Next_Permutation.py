class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 1

        def reverse(nums, left, right=index):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        for i in range(index, 0, -1):

            if nums[i - 1] >= nums[i]: continue

            left, r = i - 1, index
            while nums[r] <= nums[left]:
                r -= 1

            nums[left], nums[right] = nums[right], nums[left]
            reverse(nums, i)
            return

        nums.reverse()


nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]

Solution().nextPermutation(nums)
