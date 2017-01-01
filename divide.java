public class Solution {
    public int divide(int dividend, int divisor) {
        int count = 0;
        
        if (divisor == 0){
            return Integer.MAX_VALUE;
        }else if (dividend == 0){
            return 0;
        }
        
        if (dividend <= Integer.MIN_VALUE && divisor == -1) {
            return Integer.MAX_VALUE;
        }
        
        boolean sign = (dividend < 0 && divisor > 0) ||
        (dividend > 0 && divisor < 0);
        
        long a = Math.abs((long)dividend);
        long b = Math.abs((long)divisor);
        
        while (a >= b){
            int shift = 0;
            while (a >= (b<<shift) ){
                shift++;
            }
            count += 1<<(shift-1);
            a -= b<<(shift-1);
        }
        
        
        
        
        return sign? -count : count ;
    }
}
