public class Solution {
    public int firstMissingPositive(int[] nums) {
        int temp, size = nums.length;
        if (size < 1)
            return 1;
        
        for (int i = 0; i< size; ){
            if (nums[i] > 0 && nums[i] <= size && nums[i] != i+1 && nums[ nums[i]-1 ] != nums[i]){
                temp = nums[ nums[i]-1 ];
                nums[ nums[i] -1 ] = nums[i];
                nums[i] = temp;
            }else{
                i++;
            }
        }
        
        for (int i = 1; i <= size; i++){
            if (nums[i-1] != i)
                return i;
            
        }
        
        return size+1;
        
        
    }
}
