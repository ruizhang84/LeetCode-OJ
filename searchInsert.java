public class Solution {
    public int searchInsert(int[] nums, int target) {
        int size = nums.length;
        if (size == 0)
            return 0;
        
        int left = 0, right = size-1, mid = 0;
        while (left <= right){
            mid = (left + right)/2;
            if (nums[mid] == target){
                return mid;
            }else if (nums[mid] > target){
                right = mid-1;
            }else{
                left = mid+1;
            }
        }
        
        if ( nums[mid] < target)
            return mid+1;
        return mid;
        
        
    }
}
