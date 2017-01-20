public class Solution {
    public void rotate(int[][] matrix) {
        int size = matrix.length;
        if (size < 1)
           return;
        int temp = 0;
        for (int i = 0; i < size/2; i++){
            for (int j = 0; j < size; j++){
                temp = matrix[i][j];
                matrix[i][j] = matrix[size-1-i][j];
                matrix[size-1-i][j] = temp;
            }
        }
        
        for (int i =0; i <size-1; i++){
            for (int j = i+1; j< size; j++){
                temp = matrix[j][i];
                matrix[j][i] = matrix[i][j];
                matrix[i][j] = temp;
            }
        
        }
        
    }
}
