## 处理重复的要点是 不要在重复的数后面添加。
class Solution:
    def permuteUnique1(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i]+[n]+l[i:])
                    if i < len(l) and l[i] == n: break
            ans = new_ans
        return ans

    def permuteUnique2(self, nums):
        perms = [[]]
        for n in nums:
            perms = [
                p[:i] + [n] + p[i:] for p in perms
                for i in range((p + [n]).index(n) + 1)
            ]
        return perms


nums = [1, 2, 1]
print(Solution().permuteUnique2(nums))
