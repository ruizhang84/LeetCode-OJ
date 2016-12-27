public class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> ans = new ArrayList<String>();
        
        StringBuilder sb = new StringBuilder();
        recur_generateParenthesis(n, 0, ans, sb);
        
        return ans;
    }
    
    public void recur_generateParenthesis(int nsteps, int left, List<String> ans, StringBuilder sb) {
        if (nsteps == 0){
            for (int i = 0; i< left; i++)                       //left not matched
                sb.append(')');
            ans.add(sb.toString());
        }
        
        
        else if (nsteps > 0){
            StringBuilder sb_temp = new StringBuilder(sb);
            
            if (left >0){
                sb_temp.append(')');
                recur_generateParenthesis(nsteps, left-1, ans, sb_temp);
            }
            
            sb.append('(');
            recur_generateParenthesis(nsteps-1, left+1, ans, sb);
            
            
        }
        
        
    }
    
    
    
}
