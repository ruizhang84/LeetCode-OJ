public class Solution {
    public int longestValidParentheses(String s) {
        int size = s.length();
        if (size == 0 || size == 1)
            return 0;
        
        
        //left to right
        int potential = 0;
        int[] leftComplete = new int[size];
        int[] rightComplete = new int[size];
        
        if (s.charAt(0) == '(')
            potential = 1;
        for (int i = 1; i < size; i++){
            if (s.charAt(i) == '('){
                leftComplete[i] = leftComplete[i-1];
                potential++;
            }
            
            if (s.charAt(i) == ')'){
                if (potential > 0){
                    leftComplete[i] = leftComplete[i-1]+1;
                    potential--;
                }else{
                    leftComplete[i] = 0;
                }
            }
        }
        
        //right to left
        int max = 0;
        potential = 0;
        if (s.charAt(size-1) == ')')
            potential = 1;
            
        for (int i = size-2; i >= 0; i--){
            if (s.charAt(i) == ')'){
                if (i >= 1  && leftComplete[i] == leftComplete[i-1] + 1 )
                    rightComplete[i] = rightComplete[i+1];  //possible issue overestimate )))))
                potential++;
                
            }
            
            if (s.charAt(i) == '('){
                if (potential > 0){
                    rightComplete[i] = rightComplete[i+1]+1;
                    potential--;
                }else{
                    rightComplete[i] = 0;
                }
            }
            if (max < rightComplete[i])
                max = rightComplete[i];
        }
        
        return max*2;
        
        
        
    }
    
    
}
