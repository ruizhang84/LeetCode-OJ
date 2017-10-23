class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        
        ans = 0
        best = [0] * len(prices)
        minv = prices[0]
        maxv = prices[-1]
    
        temp_best = 0
        for i in range(len(prices)):
            temp_best, minv = maxProfitextend(temp_best, prices[i], minv, True)
            best[i] = temp_best
            
        temp_best = 0
        for i in range(len(prices)):
            temp_best, maxv = maxProfitextend(temp_best, prices[-i-1], maxv, False)
            ans  = max(ans, best[-i-1] + temp_best)
        return ans


def maxProfitextend(best, price_i, minimax, to_right):
    if to_right:
        if price_i > minimax:
            best = max(best, price_i - minimax)
        if minimax > price_i:
            minimax = price_i
        return (best, minimax)
    
    if price_i < minimax:
        best = max(best, minimax - price_i)
    if minimax < price_i:
        minimax = price_i
    return (best, minimax)
        
