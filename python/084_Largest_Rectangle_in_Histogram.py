class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0)
        ans = 0
        stack = [-1]
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
