class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0:
            return 0
        
        if len(prices) < 2:
            return 0
        elif len(prices) == 2:
            return max(0, prices[1]- prices[0])
        
        # do as much as possible
        buyq, sellq = [], []
        buy, sell = prices[0], None

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]: # sell
                sell = prices[i]
                #previous is buy
                if buy is not None: 
                    buyq.append(buy)
                    buy = None
            elif prices[i] < prices[i-1]: # buy 
                buy = prices[i]
                #previous sell
                if sell is not None:
                    sellq.append(sell)
                    sell = None

        
        if len(buyq) > len(sellq):
            if prices[-1] > buyq[-1]:
                sellq.append(prices[-1])
            else:
                buyq.pop()  
        
        if len(buyq) > k:
            res = len(buyq) - k
            for i in range(res):
                deq(buyq, sellq)        
        
        total = 0
        for i in range(len(buyq)):
            total += sellq[i] - buyq[i]
        return total
    
def deq(buyq, sellq):
    idx = 0
    cur = sellq[0] - buyq[1]
    for i in range(len(buyq)-1):
        if sellq[i] - buyq[i+1] < cur:
            cur = sellq[i] - buyq[i+1]
            idx = i
    
    cur2 = sellq[0] - buyq[0]
    idx2 = 0
    for i in range(len(buyq)):
        if sellq[i]-buyq[i] < cur2:
            cur2 = sellq[i]-buyq[i]
            idx2 = i
    
    if cur2 > cur:
        buyq[idx+1] = buyq[idx]
        sellq.pop(idx)
        buyq.pop(idx)
    else:
        sellq.pop(idx2)
        buyq.pop(idx2)
    
    return 
        
