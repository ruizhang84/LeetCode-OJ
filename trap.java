public class Solution {
    public int trap(int[] height) {
        int len = height.length;
        if (len < 2)
            return 0;
        
        int left = 0;
        int right = len-1;
        int total = 0;
        int leftbound = height[left];
        int rightbound = height[right];
        
        while (left < right){
            //process left
            while (leftbound <= rightbound && left < right){
                if (height[left] <= leftbound){
                    total += leftbound - height[left];
                    left++;
                }else{
                    leftbound = height[left];
                }
            }
            right--;
            
            while (leftbound > rightbound && left < right){
                if (height[right] <= rightbound){
                    total += rightbound - height[right];
                    right--;
                }else{
                    rightbound = height[right];
                }
            }
            left++;
        }
        
        
        return  total;
        
        
    }
}
