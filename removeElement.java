public class Solution {
    public int removeElement(int[] nums, int val) {
        int size = nums.length;
        int back = size, temp;
        
        for (int i = 0; i < size; i++){
            if (nums[i] == val){
                while (back > 1 &&nums[back-1] == val)
                    back--;
                if (i + 1 > back)
                    break;
                
                if (back > 0){
                    temp = nums[back-1];
                    nums[back-1] = nums[i];
                    nums[i] = temp;
                    back--;
                }
            }
            
        }
        
        
        return back;
        
        
        
        
    }
}
