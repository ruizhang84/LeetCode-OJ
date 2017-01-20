public class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map <String, List<String> >strList = new HashMap< String, List<String>> ();
        List<List<String>> answ = new ArrayList<List<String>> ();
        
        for (int i=0; i < strs.length; i++){
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String key = new String(chars);
            if (! strList.containsKey(key)){
                List <String> temp = new ArrayList<String> ();
                strList.put(key, temp);
            }
            strList.get(key).add(strs[i]);
            
        }
        
        for (String key: strList.keySet()){
            answ.add(strList.get(key));
            
        }
        
        return answ;
        
        
        
        
    }
}
