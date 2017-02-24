class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        if len(prices) == 0:
            return 0
        
        start = 0
        for i in range(len(prices)):
            if prices[i] < prices[start]:
                start = i
                
            if prices[i] > prices[start]:
                profit = max(profit, prices[i] -prices[start])
        
        return profit
