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
        minp1 = maxp1 = prices[0]
        minp2 = maxp2 = prices[-1]
    
        temp_best = 0
        for i in range(len(prices)):
            temp_best, minp1, maxp1 = maxProfitextend(temp_best, prices[i], minp1, maxp1, True)
            best[i] = temp_best
            
        temp_best = 0
        for i in range(len(prices)):
            temp_best, minp2, maxp2 = maxProfitextend(temp_best, prices[-i-1], minp2, maxp2, False)
            ans  = max(ans, best[-i-1] + temp_best)
        return ans


def maxProfitextend(best, price_i, minp, maxp, to_right):
    if to_right:
        if price_i > minp:
            best = max(best, price_i - minp)
        if minp > price_i:
            minp = price_i
        return (best, minp, maxp)
    
    if price_i < maxp:
        best = max(best, maxp - price_i)
    if maxp < price_i:
        maxp = price_i
    return (best, minp, maxp)
        
