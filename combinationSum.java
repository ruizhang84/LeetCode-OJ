public class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<List<Integer>> ();
        int len = candidates.length;
        if (len < 1)
            return ans;
        
        Arrays.sort(candidates);
        for (int i = 0; i < len && candidates[i] <=target; i++){
            List<Integer> temp = new ArrayList<Integer> ();
            temp.add(candidates[i]);
            recur_combinationSum(Arrays.copyOfRange(candidates, i, len), target-candidates[i], ans, temp);
        }
        
        return ans;
    }
    public void recur_combinationSum(int[] candidates, int target, List<List<Integer>> ans, List<Integer> possible) {
        if (target == 0){
            ans.add(possible);
            return;
        }
        
        int len = candidates.length;
        for (int i = 0; i < len && candidates[i] <=target; i++){
            List<Integer> temp = new ArrayList<Integer> (possible);
            temp.add(candidates[i]);
            recur_combinationSum(Arrays.copyOfRange(candidates, i, len), target-candidates[i], ans, temp);
            
        }
        
        return;
    }
    
}
