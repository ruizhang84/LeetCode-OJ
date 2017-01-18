public class Solution {
    public boolean isMatch(String s, String p){
        int sSize = s.length();
        int pSize = p.length();
        boolean ans = false;
        
        boolean match [][] = new boolean[sSize+1][pSize+1];
        match[0][0] = true;
        for (int i=1; i<= pSize; i++){
            if (p.charAt(i-1) == '*')
                match[0][i] = match[0][i-1];
            
        }
        
        for (int i= 1; i<= sSize; i++){
            for (int j=1; j<= pSize; j++){
                if (s.charAt(i-1) == p.charAt(j-1) || p.charAt(j-1) == '?'){
                    match[i][j] = match[i-1][j-1];
                    
                }else if(p.charAt(j-1) == '*'){
                    match[i][j] = match[i-1][j] || match[i][j-1];
                }
            }
        }
        
        
        return match[sSize][pSize];
        
    }
}
