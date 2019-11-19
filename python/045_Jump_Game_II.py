class Solution:
    def jump(self, nums: List[int]) -> int:
        ret = last = curr = 0
        for i in range(len(nums)):
            if(i > last):
                last = curr
                ret += 1
            curr = max(curr, i + nums[i])

        return ret
