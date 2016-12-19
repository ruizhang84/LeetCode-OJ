public class Solution {
    public List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> anws = new ArrayList<List<Integer>> ();
        
        int strlen = nums.length;
        if (strlen < 4)
            return anws;
        
        Arrays.sort(nums);
        for (int i = 0; i < strlen -3 ; i++){
            if (i != 0 && nums[i] == nums[i-1])
                continue;
            
            for (int j = i+1; j< strlen -2; j++){
                if (j != i+1 && nums[j] == nums[j-1])
                    continue;
                
                int left = j+1;
                int right = strlen-1;
                while (left < right){
                    int sum = nums[i] + nums[left] + nums[right] + nums[j];
                    if (sum == target){
                        ArrayList<Integer> tmp = new ArrayList<Integer>();
                        tmp.add(nums[i]);
                        tmp.add(nums[j]);
                        tmp.add(nums[left]);
                        tmp.add(nums[right]);
                        anws.add(tmp);
                        left++;
                        right--;
                    
                        while(left < right && nums[left -1] == nums[left])
                            left++;
                        while(left < right && nums[right +1] == nums[right])
                            right--;
                    
                    }else if (sum > target){
                        right--;
                    }else{
                        left++;
                    }
                }
            }
        }
        return anws;
        
        
    }
}
