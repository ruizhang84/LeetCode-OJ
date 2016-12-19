//Given an array S of n integers, are there elements a, b, c in S such that
//a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

public class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        List<List<Integer>> anws = new ArrayList<List<Integer>> ();
        
        int strlen = nums.length;
        if (strlen < 3)
            return anws;
        
        Arrays.sort(nums);
        for (int i = 0; i < strlen -2 ; i++){
            if (i != 0 && nums[i] == nums[i-1])
                continue;
            
            int left = i+1;
            int right = strlen-1;
            while (left < right){
                int sum = nums[i] + nums[left] + nums[right];
                if (sum == 0){
                    ArrayList<Integer> tmp = new ArrayList<Integer>();
                    tmp.add(nums[i]);
                    tmp.add(nums[left]);
                    tmp.add(nums[right]);
                    anws.add(tmp);
                    left++;
                    right--;
                    
                    while(left < right && nums[left -1] == nums[left])
                        left++;
                    while(left < right && nums[right +1] == nums[right])
                        right--;
                    
                }else if (sum > 0){
                    right--;
                }else{
                    left++;
                    
                }
            }
            
        }
        return anws;
        
        
        
    }
}
