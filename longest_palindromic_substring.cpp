#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        int pos1 = 0;
        int pos2 = 0;
        int length = s.size();
        
        /*sub strings*/
        int* seed_i = new int [length];
        int* seed_x = new int [length];
        bool* exist_i = new bool [length];
        bool* exist_x = new bool [length];
        
        for (int i = 0; i< length; i++) {
            seed_i[i] = 0;
            exist_i[i] = true;
            seed_x[i] = 0;
            exist_x[i] = true;
        }
        
        for (int j = 1; j<length; j++){
            for (int i = j; i<length-j+1; i++){
                if (exist_i[i]){
                    if(s[i-j] == s[i+j]){
                        seed_i[i] = j; //seed_i[i] = s[i-j]+seed_i[i]+s[i+j];
                        pos1 = i;
                    }else{
                        exist_i[i] = false;
                    }
                }
                
                if (exist_x[i]){
                    if(s[i-j] == s[i+j-1]){
                        seed_x[i] = j; //s[i-j]+seed_x[i]+s[i+j-1];
                        pos2 = i;
                    }else{
                        exist_x[i] = false;
                    }
                }
            }
        }
        
        if (seed_i[pos1]+1 > seed_x[pos2])
            return s.substr(pos1-seed_i[pos1], seed_i[pos1]*2+1);
        
        return s.substr(pos2-seed_x[pos2], seed_x[pos2]*2);
        
    }
};

int main(){
    Solution A;
    
    cout<<A.longestPalindrome("aaabaaaa")<<endl;
    return 0;
    
}