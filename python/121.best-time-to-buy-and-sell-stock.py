'''
@Description:
@Author: jxxiao
@Github: https://github.com/jxxiao
@Date: 2020-02-21 01:49:03
@LastEditors: jxxiao
@LastEditTime: 2020-02-23 02:26:53
'''
#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (49.33%)
# Likes:    3947
# Dislikes: 180
# Total Accepted:    719.8K
# Total Submissions: 1.5M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
#
#
# Example 2:
#
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#
#

# @lc code=start


class Solution:
    def maxProfit_1(self, prices):
        if not prices:
            return 0
        loc = glo = 0
        for i in range(1, len(prices)):
            loc = max(loc + prices[i]-prices[i-1], 0)
            glo = max(glo, loc)
        return glo

    def maxProfit(self, prices):
        if not prices:
            return 0
        buy, sell = -float('inf'), -float('inf')
        for x in prices:
            buy = max(buy, -x)
            sell = max(sell, buy + x)
        return sell

# @lc code=end
