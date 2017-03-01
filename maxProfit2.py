public class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0)
            return 0;
        
        int total = 0, minval = prices[0],  maxval = prices[0];
        for (int i = 1; i < prices.length; i ++){
            if (prices[i] > prices[i-1]){
                if (prices[i] > maxval)
                    maxval = prices[i];
                
            }else{ 
                total += maxval - minval;
                minval = maxval = prices[i];
            }
  
        }

        return maxval - minval + total;
    
    }
}
