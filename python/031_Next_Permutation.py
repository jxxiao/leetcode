class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        index = len(nums) - 1

        def reverse(nums, l, r=index):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        for i in range(index, 0, -1):

            if nums[i - 1] >= nums[i]: continue

            l, r = i - 1, index
            while nums[r] <= nums[l]:
                r -= 1

            nums[l], nums[r] = nums[r], nums[l]
            reverse(nums, i)
            return

        nums.reverse()


nums = [1, 5, 8, 4, 7, 6, 5, 3, 1]

Solution().nextPermutation(nums)
