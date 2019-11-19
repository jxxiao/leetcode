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

    def canJump2(self, nums):
        # m表示当前能去的最远的位置
        m = 0
        for i, n in enumerate(nums):
            if i > m:
                return False
            m = max(m, i + n)
        return True
