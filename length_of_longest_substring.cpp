/*
 Longest Substring Without Repeating Characters
 
 Given a string, find the length of the longest substring without repeating characters. 
 For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. 
 For "bbbbb" the longest substring is "b", with the length of 1.
*/

class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int count_table[256];
        int start = 0, ans = 0;
        int i;
        memset(count_table, -1, sizeof(count_table));
        for (i=0; i<s.length(); i++){
            if (count_table[s[i]] >=0){
                if (ans < i-start)
                    ans = i-start;
                for (int j=start; j<count_table[s[i]]; j++)
                    count_table[j] = -1;
                if (start < count_table[s[i]] +1)
                    start = count_table[s[i]] +1;
            }
            count_table[s[i]] = i;
        }
    
        if (ans < i-start) ans = i-start;
    
        return ans;
    }
    
    
};