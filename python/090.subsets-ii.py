'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-11-15 22:01:28
@LastEditors: jxxiao
@LastEditTime: 2019-11-20 16:19:37
'''
#
# @lc app=leetcode id=90 lang=python3
#
# [90] Subsets II
#
# https://leetcode.com/problems/subsets-ii/description/
#
# algorithms
# Medium (44.07%)
# Likes:    1163
# Dislikes: 56
# Total Accepted:    233.7K
# Total Submissions: 527.4K
# Testcase Example:  '[1,2,2]'
#
# Given a collection of integers that might contain duplicates, nums, return
# all possible subsets (the power set).
# 
# Note: The solution set must not contain duplicate subsets.
#
# Example:
# 
# 
# Input: [1,2,2]
# Output:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
#
#
#

# @lc code=start


class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()
        self.dfs(nums, 0, [], res)
        return res

    def dfs(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i + 1, path + [nums[i]], res)

    def subsetsWithDup_noRec(self, nums):
        nums, result, pos = sorted(nums), [[]], {}
        for n in nums:
            start, length = pos.get(n, 0), len(result)
            result += [r + [n] for r in result[start:]]
            pos[n] = length
        return result


nums = [1, 2, 2, 3, 3, 3]
Solution().subsetsWithDup(nums)
# @lc code=end
