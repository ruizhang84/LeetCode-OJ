public class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> ans = new ArrayList<Integer> ();
        if (matrix.length == 0 || matrix[0].length == 0)
            return ans;
        int left = 0, right = matrix[0].length, top = 0, down = matrix.length;
        
        int i = top, j = left;
        while(left < right && top < down){
            j = left;
            while (j < right)
                ans.add(matrix[top][j++]);
            top++;
            
            i = top;
            while(i < down)
                ans.add(matrix[i++][right-1]);
            right--;
            
            if (top >= down || left >=right)
                break;
            
            j = right-1;
            while(j >= left)
                ans.add(matrix[down-1][j--]);
            down--;
            
            i = down-1;
            while (i >= top)
                ans.add(matrix[i--][left]);
            left++;
        }
        
        return ans;
    }
}
