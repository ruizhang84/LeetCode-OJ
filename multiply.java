public class Solution {
    public String multiply(String num1, String num2) {
        int size1 = num1.length();
        int size2 = num2.length();
        StringBuilder str = new StringBuilder();
        
        if (size1 < 1 && size2 < 1)
            return "0";
        else if (size1 < 1)
            return num2;
        else if (size2 < 1)
            return num1;
        
        int carry = 0;
        int current = 0;
        //naive calculation
        for (int i=0; i<size1+size2; i++){
            current += carry;
            carry = 0;
            
            int idx= 0;
            if (i-idx > size2-1)
                idx = i-size2+1;
            
            for (; idx < size1 && i-idx >= 0 ; idx++){
                int temp1 = num1.charAt(size1-1-idx)-48;
                int temp2 = num2.charAt(size2-1-i+idx)-48;
                current += temp1*temp2%10;
                carry += temp1*temp2/10;
            }
            //System.out.print(i+ " " + current + " " + carry + "\n");
            
            if (current >= 10){
                carry += current/10;
                current = current%10;
            }
            //System.out.print("   " + current + " " + carry + "\n");
            str.insert(0,  (char) (current+48));
            current = 0;
        }
        while (str.charAt(0) == '0' && str.length() != 1)
            str.deleteCharAt(0);
        
        
        return str.toString();
        
    }
}
