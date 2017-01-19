public class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> perm = new ArrayList<List<Integer>> ();
        int size = nums.length;
        if (size < 1)
            return perm;
        
        List<Integer> temp = new ArrayList<Integer> ();
        List<Integer> visited = new ArrayList<Integer> ();
        recur_permute(nums, temp, visited, perm);
        
        return perm;
    }
    
    public void recur_permute(int [] nums, List<Integer> temp_prev, List<Integer> visited_prev, List<List<Integer>> perm){
        for (int i = 0; i< nums.length; i++){
            List<Integer> temp = new ArrayList<Integer> (temp_prev);
            List<Integer> visited = new ArrayList<Integer> (visited_prev);
            if (!visited.contains(nums[i])){
                temp.add(nums[i]);
                visited.add(nums[i]);
                recur_permute(nums, temp, visited, perm);
                if (temp.size() == nums.length)
                    perm.add(temp);
            }
        }
        
        
    }
    
    
}
