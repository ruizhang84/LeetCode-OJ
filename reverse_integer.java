import java.lang.*;
class Solution {
    public int reverse(int x) {
        StringBuilder y = new StringBuilder();
        for (int i = Math.abs(x); i > 0; i=(i-i%10)/10)
            y.append(i%10);
        
        try{
            if (x>0)
                return Integer.parseInt(y.toString());
        
            return -Integer.parseInt(y.toString());
        }catch(NumberFormatException e){
            
        }
        return 0;
    }
}

class reverse_integer{
    public static void main(String[] args){
        int a = 1230;
        Solution A = new Solution();
        System.out.println(A.reverse(a));

    }

}