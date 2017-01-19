public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> perm = new ArrayList<List<Integer>> ();
        int size = nums.length;
        if (size < 1)
            return perm;
        
        Arrays.sort(nums);
        int [] visit = new int [size];
        List<Integer> temp = new ArrayList<Integer> ();
        recur_permute(nums, temp, visit, perm);
        
        return perm;
    }
    
    public void recur_permute(int [] nums, List<Integer> temp, int [] visit, List<List<Integer>> perm){
        for (int i = 0; i< nums.length; i++){
            if (visit[i] == 1 || (i != 0 && nums[i] == nums[i-1] && visit[i-1] == 0) ) {
                continue;
            }
            visit[i] = 1;
            temp.add(nums[i]);
            recur_permute(nums, temp, visit, perm);
            
            if (temp.size() == nums.length){
                List<Integer> temp_ans = new ArrayList<Integer> (temp);
                perm.add(temp_ans);
            }
            temp.remove(temp.size()-1);
            visit[i] = 0;
        }
        
    }
}
