nums = [-1,0,1,2,-1,-4]
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3: return []
        nums.sort()
        res = set()
        #先循环从 nums[:-2]中找出一个v
        for i, v in enumerate(nums[:-2]):
            #因为已经排序过，所以v和前一个数一样的话 情况一样 直接continue
            if i >= 1 and v == nums[i-1]: continue
            d = {}
            #从nums[i+1:]中找一个x
            for x in nums[i+1:]:
                #如果这个x不在d中我们就先把-v-x添加进去 -v-x代表我们要找的第三个数 -v-x实质代表这个问题被化成了2sum
                if x not in d:
                    d[-v-x] = 1
                else:
                    res.add((v, -v-x, x))
        gen = map(list, res)
        arry = list()
        for g in gen:
            arry.append(g)

sol = Solution()

for x in sol.threeSum(nums):
    print(x)