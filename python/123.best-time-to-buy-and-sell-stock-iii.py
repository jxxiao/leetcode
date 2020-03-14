'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-02-21 02:28:35
@LastEditors: jxxiao
@LastEditTime: 2020-02-23 02:26:23
'''
#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (35.96%)
# Likes:    1640
# Dislikes: 64
# Total Accepted:    187K
# Total Submissions: 519.9K
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most two
# transactions.
#
# Note: You may not engage in multiple transactions at the same time (i.e., you
# must sell the stock before you buy again).
#
# Example 1:
#
#
# Input: [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
#
# Example 2:
#
#
# Input: [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are
# engaging multiple transactions at the same time. You must sell before buying
# again.
#
#
# Example 3:
#
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#

# @lc code=start


class Solution:
    def maxProfit_1(self, prices):
        local = 0
        globalProfit = 0
        for i in range(len(prices)):
            local = self.localProfit(prices[0:i]) + self.localProfit(
                prices[i:len(prices) + 1])
            globalProfit = max(globalProfit, local)
        return globalProfit

    def localProfit(self, prices):
        if not prices:
            return 0
        loc = glo = 0
        for i in range(1, len(prices)):
            loc = max(loc + prices[i] - prices[i - 1], 0)
            glo = max(glo, loc)
        return glo

    def maxProfit(self, prices):
        b1, s1, b2, s2 = -float('inf'), -float('inf'), -float('inf'), -float(
            'inf')
        for x in prices:
            b1, s1, b2, s2 = max(-x, b1), max(x + b1,
                                              s1), max(s1 - x,
                                                       b2), max(x + b2, s2)
        return max(0, s1, s2)


# @lc code=end
