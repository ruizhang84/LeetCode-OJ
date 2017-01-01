public class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
        List<Integer> result = new ArrayList<Integer>();
        HashMap<String, Integer> toFind = new HashMap<String, Integer>();
       
        
        int words_size = words.length, words_length = words[0].length();
        for (int i = 0; i < words_size; i ++){
            if (toFind.containsKey(words[i])){
                toFind.put(words[i], toFind.get(words[i]) + 1);
            }
            else{
                toFind.put(words[i],  1);
            }
        }
        
        for (int j = 0; j < words_length; j++){
            int start = j;
            int founded = 0;
            HashMap<String, Integer> found = new HashMap<String, Integer>();
            
            for (int i=j; i <= s.length()-words_length; i = i + words_length){
                String sub = s.substring(i, i + words_length);
                
                if (toFind.containsKey(sub)){
                    if(found.containsKey(sub)){
                        found.put(sub, found.get(sub) + 1);
                    }
                    else{
                        found.put(sub,  1);
                    }
                    
                    founded++;

                    while(found.get(sub)>toFind.get(sub)){
                        String left = s.substring(start, start + words_length);
                        found.put(left, found.get(left)-1);
                        
                        founded--;
                        start = start + words_length;
                                            }
                    if (founded == words_size){
                        result.add(start);
                        
                        String left = s.substring(start, start + words_length);
                        found.put(left, found.get(left)-1);
                        founded--;
                        start = start + words_length;
                        
                    }
                    
                    
                }else{
                    found = new HashMap<String, Integer>();
                    start = i + words_length;
                    founded = 0;
                    
                    
                }
            }
        }
    
        return result;
    }
}
