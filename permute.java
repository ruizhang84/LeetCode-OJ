public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> perm = new ArrayList<List<Integer>> ();
        int size = nums.length;
        if (size < 1)
            return perm;
        
        List<Integer> temp = new ArrayList<Integer> ();
        recur_permute(nums, temp, perm);
        
        return perm;
    }
    
    public void recur_permute(int [] nums, List<Integer> temp, List<List<Integer>> perm){
        for (int i = 0; i< nums.length; i++){
            if (!temp.contains(nums[i])){
                temp.add(nums[i]);
                recur_permute(nums, temp, perm);
                if (temp.size() == nums.length){
                    List<Integer> temp_ans = new ArrayList<Integer> (temp);
                    perm.add(temp_ans);
                }
                temp.remove(temp.size()-1);
            }
        }
        
        
    }
    
    
}
