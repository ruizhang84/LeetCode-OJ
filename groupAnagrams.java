public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> answ = new ArrayList<List<String>> ();
        int [] added = new int [strs.length];
        
        for (int i = 0; i < strs.length; i++){
            if (added[i] != 0)
                continue;
            
            List<String> temp = new ArrayList<String> ();
            temp.add(strs[i]);
            for (int j = i+1; j < strs.length; j++){
                if (strs[i].length() != strs[j].length() )
                    continue;
                temp.add(strs[j]);
                added[j] = 1;
            }
            
            if (temp.size() == 1)
                answ.add(temp);
            else
                helper_groupAnagrams(temp, answ);
            
        }
        return answ;
        
    }
    private void helper_groupAnagrams(List<String> strs, List<List<String>> answ){
        int [] added = new int [strs.size()];
        char[][] str_i = new char[strs.size()][];
        
        for (int i = 0; i < strs.size(); i++){
            str_i[i] = strs.get(i).toCharArray();
            Arrays.sort(str_i[i]);
        }
        
        for (int i = 0; i< strs.size(); i++){
            if (added[i] != 0)
                continue;
            
            List<String> temp = new ArrayList<String> ();
            temp.add(strs.get(i));
            for (int j = i+1; j < strs.size(); j++){
                if ( compare(str_i[i], str_i[j]) ){
                    temp.add( strs.get(j) );
                    added[j] = 1;
                }
                
            }
            answ.add(temp);
        }
        
    }
    
    private boolean compare(char[] s1, char[] s2){
        for (int i=0; i < s1.length; i++){
            if (s1[i] != s2[i])
                return false;
        }
        
        return true;
        
    }
}
