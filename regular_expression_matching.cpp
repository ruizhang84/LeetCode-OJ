#include <iostream>
#include <stdlib.h>

using namespace std;

class Solution {
public:
    
    bool isMatch(string s, string p) {
        int i, j;
        int slen = s.size(), plen = p.size();
        
        // empty string
        if (slen == 0){
            if (plen %2 != 0)
                return false;
            
            for (j = 0; j< plen && p[j+1] == '*'; )
                j += 2;
            
            if (j == plen)
                return true;
            return false;
        }

        //construct dynamic array dp[s_i][p_j]
        bool **dp = (bool **)malloc(slen * sizeof(bool *));
        for(i = 0; i < slen; ++i)
            //initialization
            dp[i] = (bool *)calloc(plen, sizeof(bool));
        
        //base case
        if(s[0] == p[0] || p[0] == '.')
            dp[0][0] = true;
            
        for (j = 0; j < plen-1 && p[j+1] == '*'; j += 2){
            dp[0][j+1] = true;
            if (j < plen-2 &&  (s[0] == p[j+2] || p[j+2] =='.') )
                dp[0][j+2] = true;
        }
        
        //dynamic programming
        for (i = 0; i< slen; i++){
            for (j = 0; j< plen; j++){
                if (p[j+1] == '*'){
                    if (j > 0 && i > 0 && dp[i-1][j-1] && (s[i] == p[j] || p[j] == '.'))
                        dp[i][j] = true;
                        
                    if (j > 0 && (dp[i][j-1] || dp[i][j])) //* 0 match
                        dp[i][j+1] = true;
                    
                    if (i > 0 && dp[i-1][j] && p[j] == '.')//.* match
                        dp[i][j] = true;
                    
                }else if (p[j] == '*'){
                    if (j > 0 && i > 0 && dp[i-1][j] && ( (s[i-1] == s[i] && s[i-1] == p[j-1] ) || p[j-1] == '.'))
                        dp[i][j] = true;
                }else{
                    if (j > 0 && i > 0 && dp[i-1][j-1] && (s[i] == p[j] || p[j] == '.'))
                       dp[i][j] = true;
                }
                //cout <<i<<" "<<s[i]<<" "<<j<<" "<<p[j]<<" "<<dp[i][j]<<endl;
            }
        }
        
        return dp[slen-1][plen-1];
        
        
    }
};


int main(){
    Solution A;
    //cout << A.isMatch("aaa", "aaaa") << endl;
    //cout << A.isMatch("aaa", "ab*a") << endl;
    //cout << A.isMatch("aaa", "ab*a*c*a") << endl;
    //cout << A.isMatch("aa", "a*") << endl;
    //cout << A.isMatch("a", "ab*") << endl;
    //cout << A.isMatch("aaca", "ab*a*c*a") << endl;
    //cout << A.isMatch("ab", ".*..") << endl;
    //cout << A.isMatch("", ".*") << endl;
    //cout << A.isMatch("abcdede", "ab.*de") << endl;
    //cout << A.isMatch("abb", "b*") << endl;
    //cout << A.isMatch("abb", "c*a*b*") << endl;
    cout << A.isMatch("bbcacbabbcbaaccabc", "b*a*a*.c*bb*b*.*.*") << endl;
}