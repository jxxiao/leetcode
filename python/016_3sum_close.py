class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        nums.sort()
        count = len(nums)
        distance = None
        res = None
        for i in range(count):
            head = i + 1
            tail = count - 1
            while head < tail:
                val = nums[i] + nums[head] + nums[tail]
                if distance is None or abs(val-target) < distance:
                    distance = abs(val-target)
                    res = val
                if val == target:
                    return res
                elif val < target:
                    head += 1
                else:
                    tail -= 1
        return res
