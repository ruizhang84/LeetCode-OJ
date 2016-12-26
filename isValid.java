public class Solution {
    public boolean isValid(String s) {
        if(s.length()==0||s.length()==1)
            return false;
        
        Stack<Character> st = new Stack<Character>();
        
        for (int i = 0; i<s.length(); i++){
            char curr = s.charAt(i);
            if (curr == '[' || curr  == '{' || curr  == '('){
                st.push(curr);
                
            }else if (curr  == ')'){
                
                if (st.empty()|| st.pop() != '(')
                    return false;
                
            }else if (curr  == ']'){
                if (st.empty()|| st.pop() != '[')
                    return false;
                
            }else if (curr  == '}'){
                if (st.empty()|| st.pop() != '{')
                    return false;
                
            }
            
            
            
            
        }
        
        return st.empty();
        
        
        
    }
}
