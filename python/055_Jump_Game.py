class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        step = 1
        for num in nums[-2::-1]:
            if num >= step:
                step = 1
            else:
                step += 1

        return True if step == 1 else False
