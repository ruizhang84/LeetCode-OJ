public class Solution {
    public double myPow(double x, int n) {
        if (n == 0){
            return 1.0;
        }
        if (x == 1.0)
           return 1.0;

        double sign = 1.0;
        if (x < 0){
           x = -x;
           if (n %2 != 0)
               sign = -1.0;
        }
        
        if (x == 1.0){
            return sign;
        }
        
        if (n < 0){
           if (n == -2147483648)
              return 0.0;
           n = -n;
           x = 1/x;
        }
        
        
        if (n > 1){
            double mult = 1.0;
            for (int i = 0; i < n; i++){
                mult *= x;
                if (mult < 0.00001)
                   return 0.0;
                
            }
            x = mult;
        }
        
        return x*sign;
    }
}
