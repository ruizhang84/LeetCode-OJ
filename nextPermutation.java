public class Solution {
    public void nextPermutation(int[] nums) {
        int size = nums.length;
        if (size == 0 || size == 1)
            return;
        
        int j, i;
        for (i = size -1; i > 0; i--){
            if (nums[i-1] < nums[i])
                break;
        }
        
        if (i == 0){
            Arrays.sort(nums);
            return;
        }
        
        j = size - 1;
        int least = Integer.MAX_VALUE;
        for (int k = size -1; k > i-1; k--){
            if (nums[k] < least && nums[i-1] < nums[k]){
                least = nums[k];
                j = k;
            }
        }
        
        
        int temp;
        temp = nums[i-1];
        nums[i-1] = nums[j];
        nums[j] = temp;
        
        Arrays.sort(nums, i, size);
        return;
        
        
        
    }
}
