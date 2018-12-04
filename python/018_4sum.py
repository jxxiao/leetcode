class Solution:

'''
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        results = []
        self.findNsum(nums, target, 4, [], results)
        return results

    def findNsum(self, nums, target, N, result, results):
        if len(nums) < N or N < 2:
            return

        # solve 2-sum
        if N == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    results.append(result + [nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while right > left and nums[right] == nums[right + 1]:
                        nums[right] == nums[right + 1]
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1
        else:
            for i in range(0, len(nums) - N + 1):
                if target < nums[i] * N or target > nums[-1] * N:
                    break
                if i == 0 or i > 0 and nums[
                        i - 1] != nums[i]:  # recursively reduce N
                    self.findNsum(nums[i + 1:], target - nums[i], N - 1,
                                  result + [nums[i]], results)
        return
'''

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        def findNsum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[
                    -1] * N:
                return
            if N == 2:
                left, right = 0, len(nums) - 1
                while left < right:
                    sum = nums[left] + nums[right]
                    if sum == target:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                    elif sum < target:
                        left += 1
                    else:
                        right -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i - 1] != nums[i]):
                        findNsum(nums[i + 1:], target - nums[i], N - 1,
                                 result + [nums[i]], results)

        results = []
        findNsum(sorted(nums), target, 4, [], results)
        return results
