public class Solution {
    public boolean isValid(String s) {
        Stack<Character> st = new Stack<Character>();
        
        for (int i = 0; i<s.length(); i++){
            if (s.charAt(i)  == '[' || s.charAt(i) == '{' || s.charAt(i) == '('){
                st.push(s.charAt(i));
                
            }else if (s.charAt(i) == ')'){
                
                if (st.empty()|| st.pop() != '(')
                    return false;
                
            }else if (s.charAt(i) == ']'){
                if (st.empty()|| st.pop() != '[')
                    return false;
                
            }else if (s.charAt(i) == '}'){
                if (st.empty()|| st.pop() != '{')
                    return false;
                
            }
            
            
            
            
        }
        
        return st.empty();
        
        
        
    }
}
