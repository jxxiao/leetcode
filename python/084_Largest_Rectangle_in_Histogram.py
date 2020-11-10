'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2019-05-16 19:29:22
@LastEditors: jxxiao
@LastEditTime: 2020-04-19 23:35:09
'''
class Solution:
    def largestRectangleArea(self, heights):
        ans = 0
        stack = [-1]
        heights.append(0)

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h*w)
            stack.append(i)
        heights.pop()
        return ans


heights = [2, 1, 5, 6, 2, 3]
Solution().largestRectangleArea(heights)
