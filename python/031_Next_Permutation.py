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

        # 从后往前找
        for i in range(index, 0, -1):

            # 找到一个前面一个数比后面一个数要小的地方
            if nums[i - 1] >= nums[i]: continue
            # 把后面要改变部分标出来
            left, right = i - 1, index
            # 从右往左找到第一个比left处数要大的数字
            while nums[right] <= nums[left]:
                right -= 1
            # 将这两个数位置调换
            nums[left], nums[right] = nums[right], nums[left]
            # 将left位置后面的数倒序
            reverse(nums, i)
            return nums
        # 如果是最后一个，直接把数组倒序
        nums.reverse()


nums = [3, 5, 1, 4, 2]

print(Solution().nextPermutation(nums))
