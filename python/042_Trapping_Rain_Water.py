class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        ans = 0
        for i in range(1, len(height)):
            max_left = 0
            max_right = 0
            for j in range(0, i+1):
                max_left = max(max_left, height[j])
            for j in range(i, len(height)):
                max_right = max(max_right, height[j])
            ans += min(max_left, max_right) - height[i]
        return ans

    def trap_two(self, height):
        left, right, water, minHeight = 0, len(height) - 1, 0, 0
        while left < right:
            while left < right and height[left] <= minHeight:
                water += minHeight - height[left]
                left += 1
            while right > left and height[right] <= minHeight:
                water += minHeight - height[right]
                right -= 1
            minHeight = min(height[left], height[right])
        return water


height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
Solution().trap_two(height)
