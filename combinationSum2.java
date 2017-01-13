public class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        List<List<Integer>> ans = new ArrayList<List<Integer>> ();
        int len = candidates.length;
        if (len < 1)
            return ans;
        
        Arrays.sort(candidates);
        List<Integer> candidates_set = new ArrayList<Integer>();
        Map<Integer, Integer> count = new HashMap<Integer, Integer> ();
        candidates_set.add(candidates[0]);
        int k = 1;
        int j = 1;
        for (; j < len && candidates[j] <=target; j++){
            if (candidates[j] == candidates[j-1]){
                k += 1;
            }else{
                candidates_set.add(candidates[j]);
                count.put(candidates[j-1], k);
                k = 1;
            }
        }
        count.put(candidates[j-1], k);
        
        for (int i = 0; i < candidates_set.size() && candidates_set.get(i) <=target; i++){
            List<Integer> temp = new ArrayList<Integer> ();
            temp.add(candidates_set.get(i));
            recur_combinationSum(candidates_set.subList(i, candidates_set.size()), target-candidates_set.get(i), ans, temp, count, candidates_set.get(i), 1);
        }
        
        return ans;
    }
    public void recur_combinationSum(List<Integer> candidates, int target, List<List<Integer>> ans, List<Integer> possible, Map<Integer, Integer> count, int num, int repeat) {
        if (target == 0){
            ans.add(possible);
            return;
        }
        
        int len = candidates.size();
        for (int i = 0; i < len && candidates.get(i) <=target; i++){
            List<Integer> temp = new ArrayList<Integer> (possible);
            temp.add(candidates.get(i));
            if (candidates.get(i) == num){
                if (repeat > count.get(candidates.get(i)) )
                    return;
                else if  (repeat < count.get(candidates.get(i)) )
                    recur_combinationSum(candidates.subList(i, len), target-candidates.get(i), ans, temp, count, candidates.get(i), repeat+1);
            }else
                recur_combinationSum(candidates.subList(i, len), target-candidates.get(i), ans, temp, count, candidates.get(i), 1);
            
        }
        
        return;
    }
}
