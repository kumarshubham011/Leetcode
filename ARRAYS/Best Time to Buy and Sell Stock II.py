# Find and return the maximum profit you can achieve.
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.

from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # edge case- buying and selling on same day -> profit = 0
        if not prices or len(prices) == 1:
            return 0

        profit = 0
        # take down all daily returns and sum up all positive returns
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]
        return profit
