/* ZigZag Conversion*/
class Solution {
    public String convert(String s, int numRows) {
        int len = s.length();
        if (numRows == 1)
            return s;
        
        StringBuilder str = new StringBuilder();
        int strSize = 2*numRows-2;
        for (int i=0; i< numRows; i++){    //row
            for (int j=i; j<len; j+=strSize){  //diagonal number
                str.append(s.charAt(j));
                if (i != 0 && i != numRows - 1){
                    int temp = j+strSize-2*i;
                    if(temp < len)
                        str.append(s.charAt(temp));
                }
            }
        }
        return str.toString();
    }
}

class zigzag{
    public static void main(String [] args){
        String str = "12345678";
        Solution A = new Solution ();
        System.out.println(A.convert(str, 5));
    }
    
}


