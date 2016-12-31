public class Solution {
    public int removeDuplicates(int[] nums) {
        int size = nums.length, count = 1;
        if (size == 0 || size == 1)
            return size;
        
        for (int i = 0; i < size-1; i++){
            if (nums[i] != nums[i+1])
                nums[count++] = nums[i+1];
            
        }
        
        
        return count;
    }
}
