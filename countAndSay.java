public class Solution {
    public String countAndSay(int n) {
        if (n < 1)
            return "";
        else if (n == 1)
            return "1";
        
        String s = new String("1");
        for (int i = 0; i< n-1; i++){
            StringBuilder sb = new StringBuilder();
            int k = 0;      //repreate element
            for (int j = 0; j < s.length()-1; j++){
                if (s.charAt(j) == s.charAt(j+1)){
                    k++;
                }else{
                    if (k > 0){
                        sb.append(k+1);
                        k = 0;
                    }else{
                        sb.append('1');
                    }
                    sb.append(s.charAt(j));
                }
            }
            //System.out.println(k + "   " +sb.toString());
            if (k > 0){
                sb.append(k+1);
                k = 0;
            }else{
                sb.append('1');
            }
            sb.append(s.charAt(s.length()-1));
            s = sb.toString();
            //System.out.println("here" + s);
            
        }
        
        return s;
        
    }
}
