#include <stdio.h>

#define INT_MAX 2147483647
#define INT_MIN -2147483648

int myAtoi(char* str) {
    int i, n = 0, sign = 0, sign_pos = 0, sign_neg = 0;
    
    // prepocessing +/-
    for (i = 0; str[i] != '\0'; i++){
        if (str[i] == 45){
            sign_neg -= 1;
        }else if (str[i] == 43) {
            sign_pos += 1;
        }else if (str[i] == 32 && sign_pos == 0 && sign_neg == 0) {
            continue;
        }else if (str[i]>47 && str[i]<58){
            break;
        }else{
            return 0;
        }
    }

    // demine +/-
    if (sign_pos > 1 || sign_neg < -1){
        return 0;
    }else if (sign_pos == 1 && sign_neg == 1){
        return 0;
    }else if (sign_pos == 0 && sign_neg == 0){
        sign = 1;
    }else{
        sign = sign + sign_pos + sign_neg;
    }
    
    // recording 123...
    for (i; str[i] != '\0'; i++){
        if (str[i]>47 && str[i]<58){
            if (n >INT_MAX/10 || n == INT_MAX/10 && str[i]-48 > 7){
                return INT_MAX;
            }else if (n < INT_MIN/10 || n == INT_MIN/10 && str[i]-48 > 8){
                return INT_MIN;
            }
            n = n*10 + (str[i]-48)*sign;
        }else{
            return n;
        }
    }
    
    return n;
}


int main(){
    char a[] = "   - 321";
    printf ("stirng is %d \n", myAtoi(a));
    return 0;
}
