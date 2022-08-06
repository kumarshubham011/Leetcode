from ast import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # we will use two pointer l,r initialise it to 0 and 1
        # take profit as 0,take a while loop till right reaches end of list
        # if left is greater than right means there will be loss for sure, so we increment the left and right pointer
        # we calc the current profit by subtracting left from right, if it is greater than profit we update it and increment our left and update right pointer each time so that it points to only one index after right element
        profit = 0
        l, r = 0, 1
        while r < len(prices):
            curr_profit = prices[r] - prices[l]
            if prices[r] > prices[l]:
                profit = max(profit, curr_profit)
            else:
                l = r
            r += 1
        return profit
