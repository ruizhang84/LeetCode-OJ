public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int size = nums.length;
        int[] ans = new int[2];
        
        if (size == 0){
            ans[0] = -1;
            ans[1] = -1;
            return ans;
        }
        
        int left = 0, right = size-1, mid = 0;
        while (left <= right){
            mid = (left + right)/2;
            if (nums[mid] == target){
                break;
            }else if (nums[mid] > target){
                right = mid-1;
            }else{
                left = mid+1;
            }
        }
        
        if (left > right){
            ans[0] = -1;
            ans[1] = -1;
            return ans;
        }
        
        
        while(left <= mid){
            if (nums[left] == target)
                break;
            left++;
        }
        
        
        
        while(right >= mid){
            if (nums[right] == target)
                break;
            right--;
        }
        
        
        
        ans[0] = left;
        ans[1] = right;
        
        return ans;
        
        
        
        
    }
}
