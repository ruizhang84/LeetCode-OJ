/* Palindrome Number */
import java.lang.*;

class Solution {
    public boolean isPalindrome(int x) {
        // simple case
        if (x < 0){
            return false;
        }
        
        //measure the number of x n
        int n = (int) Math.log10(x);
        //System.out.println(n);
        
        //compare x.., ..x
        for (int i=0; i<n/2+1; i++){
            if (x/(int) Math.pow(10, i)%10 !=  x/(int) Math.pow(10, n-i)%10)
                return false;
            //System.out.format("The value of i is: %d and %d\n", x/(int) Math.pow(10, i)%10,
            //                  x/(int) Math.pow(10, n-i)%10 );
        }
        return true;
    }
}



class palindrome_number{
    public static void main(String [] args){
        int a = 10;
        Solution A = new Solution ();
        System.out.println(A.isPalindrome(a)? "the number is palindrome.": "no.");
        }
}


