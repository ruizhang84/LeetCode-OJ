public class Solution {
    public int strStr(String haystack, String needle) {
        int haystack_size = haystack.length();
        int needle_size = needle.length();
        
        if (needle_size > haystack_size)
            return -1;
        if (needle_size == 0)
            return 0;
        
        for (int i = 0, j = 0, k = 0; i < haystack_size-needle_size +1;){
            if (needle.charAt(j) == haystack.charAt(k)){
                j++;
                k++;
            }else{
                j = 0;
                i++;
                k = i;
            }
            
            if (j > needle_size-1)
                return i;
            
            if (k > haystack_size-1)
                return -1;
            
        }
        
        return -1;
        
        
    }
}
